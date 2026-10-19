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

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import banner  # noqa: E402
import cards  # noqa: E402
import languages  # noqa: E402
import radar  # noqa: E402
import sync_readme  # noqa: E402
from svgkit import ASSETS, current_version  # noqa: E402


def generate_all() -> None:
    banner.main()
    radar.main()
    cards.main()
    languages.main()


def snapshot() -> dict[str, str]:
    """Contenido actual de los SVG versionados."""
    return {path.name: path.read_text(encoding="utf-8") for path in ASSETS.glob("*.v*.svg")}


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
        sync_readme.sync()
        print("Listo.")
        return

    print("Generando los SVG del perfil…")
    before = snapshot()
    generate_all()
    after = snapshot()

    if before != after:
        version = sync_readme.bump()
        print(f"  · el contenido cambió → versión v{version}")
        generate_all()
        remove_stale(version)
    else:
        print(f"  · sin cambios (se mantiene la versión v{current_version()})")

    sync_readme.sync()
    print("Listo.")


if __name__ == "__main__":
    main()
