"""Genera el radar de habilidades del perfil.

Dibuja un gráfico de araña con dos series: lo que ya está en producción y lo
que está en investigación. Los valores viven en ``assets/skills.json``.

Salida:
    assets/radar-dark.svg
    assets/radar-light.svg

Uso:
    python scripts/radar.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import (  # noqa: E402
    ASSETS, THEMES, circle, gradient, line, load_json, polygon, save_svg, text,
)

WIDTH = 620
HEIGHT = 545
CENTER_X = WIDTH / 2
CENTER_Y = 280
RADIUS = 158
RINGS = 5
LABEL_RADIUS = RADIUS + 34


def axis_point(index: int, total: int, ratio: float) -> tuple[float, float]:
    """Punto en el eje ``index`` de un total de ``total``, a ``ratio`` del radio."""
    angle = -math.pi / 2 + (2 * math.pi * index / total)
    return (
        CENTER_X + math.cos(angle) * RADIUS * ratio,
        CENTER_Y + math.sin(angle) * RADIUS * ratio,
    )


def build(theme) -> str:
    data = load_json("skills.json")
    axes: list[str] = data["axes"]
    series: list[dict] = data["series"]
    total = len(axes)

    body: list[str] = []

    # Un degradado por serie: cada polígono se rellena con su propio color.
    for index, spec in enumerate(series):
        color = theme.color(spec.get("color", "accent"))
        body.append(
            gradient(
                f"series-{theme.name}-{index}",
                [(0.0, color, 0.34), (1.0, color, 0.10)],
            )
        )

    # --- rejilla ----------------------------------------------------------
    for ring in range(1, RINGS + 1):
        ratio = ring / RINGS
        points = [axis_point(i, total, ratio) for i in range(total)]
        body.append(polygon(points, fill="none", stroke=theme.grid, stroke_width=1))

    for index in range(total):
        x, y = axis_point(index, total, 1)
        body.append(line(CENTER_X, CENTER_Y, x, y, stroke=theme.grid, stroke_width=1))

    # --- series ------------------------------------------------------------
    for index, spec in enumerate(series):
        color = theme.color(spec.get("color", "accent"))
        values = spec["values"]
        points = []
        for axis, value in enumerate(values):
            ratio = max(0.0, min(1.0, value / 100.0))
            points.append(axis_point(axis, total, ratio))
        body.append(
            polygon(
                points,
                fill=f"url(#series-{theme.name}-{index})",
                stroke=color,
                stroke_width=2,
            )
        )
        for point in points:
            body.append(circle(point[0], point[1], 3.5, fill=color))

    # --- ejes y etiquetas ---------------------------------------------------
    for index, label in enumerate(axes):
        angle = -math.pi / 2 + (2 * math.pi * index / total)
        x = CENTER_X + math.cos(angle) * LABEL_RADIUS
        y = CENTER_Y + math.sin(angle) * LABEL_RADIUS
        anchor = "middle"
        if abs(math.cos(angle)) > 0.3:
            anchor = "start" if math.cos(angle) > 0 else "end"
        body.append(
            text(x, y + 4, label, size=12.5, weight=600, fill=theme.text, anchor=anchor)
        )

    # --- leyenda ------------------------------------------------------------
    legend_y = HEIGHT - 34
    offset = 0
    for spec in series:
        color = theme.color(spec.get("color", "accent"))
        body.append(circle(CENTER_X - 108 + offset, legend_y - 4, 5, fill=color))
        body.append(
            text(CENTER_X - 96 + offset, legend_y, spec["name"], size=12.5, fill=theme.muted)
        )
        offset += 34 + len(spec["name"]) * 6.9

    # --- título --------------------------------------------------------------
    body.append(
        text(CENTER_X, 30, data.get("title", ""), size=17, weight=700,
             fill=theme.text, anchor="middle")
    )
    if data.get("subtitle"):
        body.append(
            text(CENTER_X, 50, data["subtitle"], size=12.5, fill=theme.muted, anchor="middle")
        )

    return "".join(body)


def main() -> None:
    for key, theme in THEMES.items():
        path = save_svg(
            f"radar", WIDTH, HEIGHT, build(theme), theme,
            title="Radar de habilidades técnicas",
            desc="Gráfico de araña con dos series: habilidades en producción y en investigación.",
        )
        print(f"  ✓ {path.relative_to(ASSETS.parent)}")


if __name__ == "__main__":
    main()
