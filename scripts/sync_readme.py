"""Sincroniza las referencias a los assets del README con la versión actual.

GitHub cachea los SVG embebidos en un README durante largos periodos. Por eso
los assets llevan la versión en el nombre (``banner-dark.v1.svg``). Cuando se
regenera el contenido, hay que subir el número de versión y reescribir las
referencias del README.

Uso:
    python scripts/sync_readme.py            # alinea el README con la versión actual
    python scripts/sync_readme.py --bump     # sube la versión y alinea el README
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import ASSETS, VERSION_FILE, current_version  # noqa: E402

README = ASSETS.parent / "README.md"

# assets/<base>-<theme>.v<num>.svg   (theme = dark | light)
PATTERN = re.compile(r"assets/([a-z0-9.\-]+)-(dark|light)\.v(\d+)\.svg")


def bump() -> int:
    """Sube la versión en ``assets/version.json`` y la devuelve."""
    version = current_version() + 1
    VERSION_FILE.write_text(
        json.dumps({"version": version}, indent=2) + "\n", encoding="utf-8"
    )
    return version


def sync() -> int:
    """Reescribe las referencias del README con la versión actual."""
    if not README.exists():
        print(f"No se encontró {README.name}; se omite la sincronización.")
        return current_version()

    version = current_version()
    original = README.read_text(encoding="utf-8")
    updated = PATTERN.sub(
        lambda match: f"assets/{match.group(1)}-{match.group(2)}.v{version}.svg",
        original,
    )

    if updated != original:
        README.write_text(updated, encoding="utf-8")
        print(f"  ✓ README actualizado a la versión v{version}")
    else:
        print(f"  · README ya apuntaba a la versión v{version}")

    return version


def main() -> None:
    if "--bump" in sys.argv:
        version = bump()
        print(f"Versión de assets subida a v{version}.")
    else:
        version = current_version()
    sync()


if __name__ == "__main__":
    main()
