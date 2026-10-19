"""Compone las capturas de ``images/`` en un contact sheet para revisarlas.

Herramienta de desarrollo: no forma parte del repositorio publicado.

Uso:
    python scripts/contact_sheet.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import ROOT  # noqa: E402

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Necesitas Pillow: pip install pillow")
    raise SystemExit(1)

SOURCE = ROOT / "images"
OUTPUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "contact-sheet.png"

COLS = 3
CELL_W = 460
PAD = 10
LABEL_H = 26


def main() -> None:
    files = sorted(SOURCE.glob("*.png"))
    if not files:
        print("No hay capturas en images/")
        return

    thumbs = []
    for path in files:
        image = Image.open(path).convert("RGB")
        ratio = CELL_W / image.width
        thumb = image.resize((CELL_W, int(image.height * ratio)))
        thumbs.append((path.name, thumb))

    cell_h = max(t.height for _, t in thumbs) + LABEL_H
    rows = (len(thumbs) + COLS - 1) // COLS
    sheet = Image.new(
        "RGB",
        (COLS * (CELL_W + PAD) + PAD, rows * (cell_h + PAD) + PAD),
        "#0d1117",
    )
    draw = ImageDraw.Draw(sheet)

    for index, (name, thumb) in enumerate(thumbs):
        col = index % COLS
        row = index // COLS
        x = PAD + col * (CELL_W + PAD)
        y = PAD + row * (cell_h + PAD)
        draw.text((x + 4, y + 6), name, fill="#e6edf3")
        sheet.paste(thumb, (x, y + LABEL_H))

    sheet.save(OUTPUT)
    print(f"{OUTPUT}  ({sheet.width}x{sheet.height})")


if __name__ == "__main__":
    main()
