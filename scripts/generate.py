"""Genera todos los SVG del perfil de una sola vez.

Uso:
    python scripts/generate.py           # regenera los assets
    python scripts/generate.py --bump    # fuerza el cambio de versión

Cada script individual (``banner.py``, ``radar.py``, ``cards.py``,
``languages.py``) también se puede ejecutar por separado.

El versionado existe porque GitHub cachea los SVG embebidos en un README
durante largos periodos. Cuando el contenido cambia de verdad, el generador
sube solo la versión y reescribe las referencias del README; cuando nada
cambia, no genera ruido.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import banner  # noqa: E402
import cards  # noqa: E402
import languages  # noqa: E402
import radar  # noqa: E402
import sync_readme  # noqa: E402
from svgkit import ASSETS, current_version  # noqa: E402

STATE_FILE = ASSETS / "state.json"


def generate_all() -> None:
    banner.main()
    radar.main()
    cards.main()
    languages.main()


def logical_name(filename: str) -> str:
    """`banner-dark.v3.svg` -> `banner-dark` (sin la versión)."""
    parts = filename.split(".v")
    return parts[0] if len(parts) > 1 else filename


def fingerprints() -> dict[str, str]:
    """Huella del contenido de cada asset, indexada por nombre lógico.

    El contenido del SVG no depende de la versión (sólo el nombre del
    archivo), así que la huella compara el *qué* con el *cómo se llama*.
    """
    result: dict[str, str] = {}
    for path in ASSETS.glob("*.v*.svg"):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        result[logical_name(path.name)] = digest
    return result


def load_state() -> dict[str, str]:
    """Huellas de la última generación conocida."""
    if not STATE_FILE.exists():
        return {}
    with STATE_FILE.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def save_state(state: dict[str, str]) -> None:
    STATE_FILE.write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def remove_stale(version: int) -> None:
    """Borra los SVG de versiones anteriores a la actual."""
    for path in ASSETS.glob("*.v*.svg"):
        if f".v{version}.svg" not in path.name:
            path.unlink()
            print(f"  · eliminado {path.name}")


def main() -> None:
    forced = "--bump" in sys.argv

    if forced:
        version = sync_readme.bump()
        print(f"Versión de assets: v{version}")
        generate_all()
        remove_stale(version)
        save_state(fingerprints())
        sync_readme.sync()
        print("Listo.")
        return

    print("Generando los SVG del perfil…")
    generate_all()
    current = fingerprints()

    if current != load_state():
        version = sync_readme.bump()
        print(f"  · el contenido cambió → versión v{version}")
        generate_all()
        remove_stale(version)
        save_state(fingerprints())
    else:
        print(f"  · sin cambios (se mantiene la versión v{current_version()})")

    sync_readme.sync()
    print("Listo.")


if __name__ == "__main__":
    main()
