"""Genera las tarjetas de métricas (KPI) del perfil.

Los datos viven en ``assets/stats.json``.

Salida:
    assets/card-stats-dark.svg
    assets/card-stats-light.svg

Uso:
    python scripts/cards.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import (  # noqa: E402
    ASSETS, THEMES, line, load_json, rect, save_svg, text,
)

TILE_W = 220
TILE_H = 132
GAP = 18
MARGIN = 18
HEADER_H = 74


def build(theme) -> tuple[str, int, int]:
    data = load_json("stats.json")
    tiles = data["tiles"]

    columns = 2
    rows = (len(tiles) + columns - 1) // columns
    width = MARGIN * 2 + columns * TILE_W + (columns - 1) * GAP
    height = MARGIN * 2 + HEADER_H + rows * TILE_H + (rows - 1) * GAP

    body: list[str] = []

    body.append(rect(0, 0, width, height, fill=theme.bg, rx=14))
    body.append(rect(0.5, 0.5, width - 1, height - 1, fill="none",
                     stroke=theme.border, rx=14, stroke_width=1))

    body.append(
        text(MARGIN, MARGIN + 22, data.get("title", ""), size=17, weight=700, fill=theme.text)
    )
    if data.get("subtitle"):
        body.append(
            text(MARGIN, MARGIN + 44, data["subtitle"], size=12.5, fill=theme.muted)
        )
    body.append(line(MARGIN, MARGIN + 58, width - MARGIN, MARGIN + 58,
                     stroke=theme.border, stroke_width=1))

    for index, tile in enumerate(tiles):
        column = index % columns
        row = index // columns
        x = MARGIN + column * (TILE_W + GAP)
        y = MARGIN + HEADER_H + row * (TILE_H + GAP)

        body.append(rect(x, y, TILE_W, TILE_H, fill=theme.surface, rx=10))
        body.append(rect(x, y, 3, TILE_H, fill=theme.accent, rx=1.5))

        body.append(
            text(x + 20, y + 52, tile["value"], size=38, weight=700, fill=theme.text)
        )
        body.append(
            text(x + 20, y + 78, tile["label"], size=13.5, weight=600, fill=theme.text)
        )
        body.append(
            text(x + 20, y + 99, tile.get("hint", ""), size=11.5, fill=theme.muted)
        )

    return "".join(body), width, height


def main() -> None:
    for key, theme in THEMES.items():
        body, width, height = build(theme)
        path = save_svg(
            f"card-stats", width, height, body, theme,
            title="Métricas del portafolio",
            desc="Tarjetas con el número de proyectos, despliegues en producción, repos públicos y cobertura.",
        )
        print(f"  ✓ {path.relative_to(ASSETS.parent)}")


if __name__ == "__main__":
    main()
