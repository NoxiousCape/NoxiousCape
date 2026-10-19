"""Genera el gráfico de lenguajes del perfil.

Barras horizontales con el volumen de código por lenguaje. Los repos públicos
se miden con la API de GitHub; los privados son estimaciones declaradas en
``assets/languages.json``.

Salida:
    assets/metrics.languages-dark.svg
    assets/metrics.languages-light.svg

Uso:
    python scripts/languages.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import (  # noqa: E402
    ASSETS, THEMES, circle, line, load_json, rect, save_svg, text,
)

WIDTH = 560
MARGIN = 24
BAR_X = 132
BAR_W = 268
ROW_H = 30
HEADER_H = 92
FOOTER_H = 34
TOP_LANGUAGES = 10


def build(theme) -> tuple[str, int, int]:
    data = load_json("languages.json")
    colors: dict[str, str] = data.get("colors", {})

    totals: dict[str, int] = {}
    for group in ("public", "private"):
        for language, size in data.get(group, {}).items():
            totals[language] = totals.get(language, 0) + size

    ordered = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    shown = ordered[:TOP_LANGUAGES]
    hidden = ordered[TOP_LANGUAGES:]

    rows = len(shown)
    height = MARGIN * 2 + HEADER_H + rows * ROW_H + FOOTER_H

    body: list[str] = []
    body.append(rect(0, 0, WIDTH, height, fill=theme.bg, rx=14))
    body.append(rect(0.5, 0.5, WIDTH - 1, height - 1, fill="none",
                     stroke=theme.border, rx=14, stroke_width=1))

    body.append(
        text(MARGIN, MARGIN + 24, data.get("title", ""), size=16.5, weight=700, fill=theme.text)
    )
    if data.get("subtitle"):
        body.append(
            text(MARGIN, MARGIN + 45, data["subtitle"], size=12, fill=theme.muted)
        )
    body.append(line(MARGIN, MARGIN + 58, WIDTH - MARGIN, MARGIN + 58,
                     stroke=theme.border, stroke_width=1))

    largest = shown[0][1] if shown else 1
    for index, (language, size) in enumerate(shown):
        y = MARGIN + HEADER_H + index * ROW_H
        color = colors.get(language, theme.muted)

        body.append(circle(MARGIN + 5, y - 4, 5, fill=color))
        body.append(text(MARGIN + 18, y, language, size=12.5, weight=600, fill=theme.text))

        ratio = size / largest if largest else 0
        width = max(4.0, BAR_W * ratio)
        body.append(rect(BAR_X, y - 13, BAR_W, 11, fill=theme.grid, rx=5.5))
        body.append(rect(BAR_X, y - 13, width, 11, fill=color, rx=5.5))

        body.append(
            text(WIDTH - MARGIN, y, f"{size / 1000:.0f}k", size=11.5,
                 fill=theme.muted, anchor="end")
        )

    if hidden:
        others = sum(size for _, size in hidden)
        y = MARGIN + HEADER_H + rows * ROW_H + 4
        body.append(
            text(MARGIN, y, f"+ {len(hidden)} más: {others / 1000:.0f}k líneas",
                 size=11.5, fill=theme.muted)
        )

    return "".join(body), WIDTH, height


def main() -> None:
    for key, theme in THEMES.items():
        body, width, height = build(theme)
        path = save_svg(
            f"metrics.languages", width, height, body, theme,
            title="Lenguajes por volumen de código",
            desc="Barras horizontales con el volumen estimado de código por lenguaje en todos los proyectos.",
        )
        print(f"  ✓ {path.relative_to(ASSETS.parent)}")


if __name__ == "__main__":
    main()
