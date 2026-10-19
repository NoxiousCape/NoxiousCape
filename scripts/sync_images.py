"""Integra las capturas de ``images/`` en el README.

Cada captura se optimiza a **WebP**, se recorta al ancho máximo definido y se
publica en ``assets/shots/<nombre>.v<N>.webp``. La versión sube sólo cuando
el contenido cambia, y las referencias del README se reescriben solas.

El resultado: las 13 capturas pesan **0,5 MB** en vez de 6,2 MB, y cada
archivo se sirve una sola vez aunque aparezca en dos sitios del README
(la galería y la ficha del proyecto).

Uso:
    python scripts/sync_images.py

Requiere Pillow (ver ``requirements-dev.txt``).
"""

from __future__ import annotations

import hashlib
import io
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import ASSETS, ROOT  # noqa: E402

try:
    from PIL import Image
except ImportError:
    print("Falta Pillow. Instálalo con:  pip install -r requirements-dev.txt")
    raise SystemExit(1) from None

MANIFEST = ASSETS / "images.json"
SOURCE_DIR = ROOT / "images"
README = ROOT / "README.md"

# Referencia a una captura en el README: assets/shots/<nombre>.v<N>.webp
REFERENCE = re.compile(r"assets/shots/([a-z0-9\-]+)\.v(\d+)\.webp")


def load_manifest() -> dict:
    with MANIFEST.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def optimize(source: Path, max_width: int, quality: int) -> bytes:
    """Recorta al ancho máximo y devuelve el WebP comprimido."""
    with Image.open(source) as original:
        image = original.convert("RGB")
        if image.width > max_width:
            ratio = max_width / image.width
            image = image.resize((max_width, int(image.height * ratio)))
        buffer = io.BytesIO()
        image.save(buffer, format="WEBP", quality=quality, method=6)
        return buffer.getvalue()


def render(manifest: dict, version: int) -> dict[str, str]:
    """Genera los WebP y devuelve la huella de cada uno."""
    out_dir = ASSETS / manifest.get("output_dir", "shots")
    out_dir.mkdir(parents=True, exist_ok=True)
    max_width = manifest.get("max_width", 1600)
    quality = manifest.get("quality", 88)

    fingerprints: dict[str, str] = {}
    for name, spec in manifest["shots"].items():
        source = SOURCE_DIR / spec["source"]
        if not source.exists():
            print(f"  ! falta {source.name} para '{name}'; se omite")
            continue

        payload = optimize(source, max_width, quality)
        target = out_dir / f"{name}.v{version}.webp"
        target.write_bytes(payload)
        fingerprints[f"shot-{name}"] = hashlib.sha256(payload).hexdigest()
        print(f"  ✓ {target.name:<28} {len(payload)/1024:>6.0f} KB")

    return fingerprints


def remove_stale(version: int) -> None:
    out_dir = ASSETS / "shots"
    for path in out_dir.glob("*.webp"):
        if f".v{version}.webp" not in path.name:
            path.unlink()
            print(f"  · eliminado {path.name}")


def sync_readme(version: int) -> None:
    if not README.exists():
        return
    original = README.read_text(encoding="utf-8")
    updated = REFERENCE.sub(
        lambda match: f"assets/shots/{match.group(1)}.v{version}.webp", original
    )
    if updated != original:
        README.write_text(updated, encoding="utf-8", newline="\n")
        print(f"  ✓ README actualizado a la versión v{version}")


def main() -> None:
    manifest = load_manifest()
    version = manifest.get("version", 1)

    print("Optimizando las capturas…")
    fingerprints = render(manifest, version)

    # Huellas de la generación anterior: si no cambia nada, no se toca nada.
    state_path = ASSETS / "images-state.json"
    previous = {}
    if state_path.exists():
        with state_path.open(encoding="utf-8-sig") as handle:
            previous = json.load(handle)

    if fingerprints != previous:
        version += 1
        manifest["version"] = version
        MANIFEST.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(f"  · el contenido cambió → versión v{version}")
        fingerprints = render(manifest, version)
        remove_stale(version)
    else:
        print(f"  · sin cambios (se mantiene la versión v{version})")

    state_path.write_text(
        json.dumps(fingerprints, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    sync_readme(version)

    total = sum(p.stat().st_size for p in (ASSETS / "shots").glob("*.webp"))
    print(f"  → {total/1024/1024:.2f} MB en total")


if __name__ == "__main__":
    main()
