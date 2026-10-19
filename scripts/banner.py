"""Genera el banner del perfil: una terminal SVG con el "whoami" del autor.

El contenido NO está en este archivo sino en ``assets/banner.json``, para que
puedas editar el texto sin tocar Python.

Salida:
    assets/banner-dark.svg
    assets/banner-light.svg

Uso:
    python scripts/banner.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import (  # noqa: E402
    ASSETS, MONO, THEMES, circle, esc, gradient, line, load_json, rect,
    save_svg, text,
)

WIDTH = 740
PADDING_X = 26
PADDING_TOP = 58
LINE_HEIGHT = 24
TITLEBAR_HEIGHT = 38
RADIUS = 12

# Colores por clase semántica del JSON.
CLASS_COLORS = {
    "prompt": "accent",
    "cmd": "text",
    "strong": "text",
    "text": "text",
    "muted": "muted",
    "key": "accent2",
    "ok": "accent",
}

# Clases que se dibujan en negrita.
BOLD_CLASSES = {"cmd", "strong"}

# Semáforo de la terminal (colores estilo macOS, legibles en ambos temas).
TRAFFIC_LIGHTS = ("#ff5f57", "#febc2e", "#28c840")

# El parser de XML colapsa los espacios al inicio y al final de un <text>.
# Por eso cada palabra se dibuja como un <text> propio, con su posición
# calculada a partir del índice de columna: nada depende de la conservación
# de espacios en blanco.
TOKEN_RE = re.compile(r"(\S+|\s+)")


def build(theme) -> tuple[str, int]:
    data = load_json("banner.json")
    lines = data["lines"]
    font_size = data.get("font_size", 14.5)
    char_width = data.get("char_width", 8.6)

    content_height = len(lines) * LINE_HEIGHT
    height = PADDING_TOP + content_height + 22

    body: list[str] = []

    # --- fondo y marco ----------------------------------------------------
    body.append(
        gradient(
            f"bar-{theme.name}",
            [(0.0, theme.accent, 1.0), (0.5, theme.accent2, 1.0), (1.0, theme.accent4, 1.0)],
        )
    )
    body.append(rect(0, 0, WIDTH, height, fill=theme.bg, rx=RADIUS))
    body.append(rect(0.5, 0.5, WIDTH - 1, height - 1, fill="none",
                     stroke=theme.border, rx=RADIUS, stroke_width=1))

    # Recorte redondeado para la franja de acento
    body.append(
        f'<clipPath id="frame-{theme.name}">'
        f'<rect x="0" y="0" width="{WIDTH}" height="{height}" rx="{RADIUS}"/></clipPath>'
    )

    # --- barra de título ---------------------------------------------------
    body.append(
        f'<path d="M {RADIUS} 0 H {WIDTH - RADIUS} A {RADIUS} {RADIUS} 0 0 1 {WIDTH} {RADIUS} '
        f'V {TITLEBAR_HEIGHT} H 0 V {RADIUS} A {RADIUS} {RADIUS} 0 0 1 {RADIUS} 0 Z" '
        f'fill="{theme.titlebar}"/>'
    )
    body.append(line(0, TITLEBAR_HEIGHT, WIDTH, TITLEBAR_HEIGHT,
                     stroke=theme.border, stroke_width=1, cap="butt"))

    # Semáforo de la terminal
    for index, color in enumerate(TRAFFIC_LIGHTS):
        body.append(circle(PADDING_X + index * 18, TITLEBAR_HEIGHT / 2, 5.5, fill=color))

    body.append(
        text(
            WIDTH / 2, TITLEBAR_HEIGHT / 2 + 4.5,
            data.get("window_title", ""),
            size=12.5, fill=theme.muted, anchor="middle", family=MONO,
        )
    )

    # Franja de acento superior
    body.append(
        f'<rect x="0" y="0" width="{WIDTH}" height="3" fill="url(#bar-{theme.name})" '
        f'clip-path="url(#frame-{theme.name})"/>'
    )

    # --- líneas de la terminal --------------------------------------------
    for row, segments in enumerate(lines):
        y = PADDING_TOP + row * LINE_HEIGHT
        if not segments:
            continue
        column = 0
        for segment in segments:
            content = segment.get("t", "")
            if not content:
                continue
            style = segment.get("c", "text")
            fill = theme.color(CLASS_COLORS.get(style, "text"))
            weight = 700 if style in BOLD_CLASSES else 400
            for token in TOKEN_RE.findall(content):
                if token.isspace():
                    column += len(token)
                    continue
                body.append(
                    text(
                        PADDING_X + column * char_width, y,
                        token, size=font_size, fill=fill, family=MONO, weight=weight,
                    )
                )
                column += len(token)

    # Cursor parpadeante al final
    last_row = len(lines) - 1
    while last_row >= 0 and not lines[last_row]:
        last_row -= 1
    if last_row >= 0:
        column = sum(len(seg.get("t", "")) for seg in lines[last_row])
        body.append(
            rect(
                PADDING_X + column * char_width, PADDING_TOP + last_row * LINE_HEIGHT - font_size + 3,
                char_width * 0.6, font_size + 2, fill=theme.accent, opacity=0.85,
            )
        )

    return "".join(body), height


def main() -> None:
    for key, theme in THEMES.items():
        body, height = build(theme)
        path = save_svg(
            f"banner", WIDTH, height, body, theme,
            title="Terminal con el perfil de Daniel Páez",
            desc="Muestra nombre, stack técnico, enfoque de trabajo y resumen del portafolio.",
        )
        print(f"  ✓ {path.relative_to(ASSETS.parent)}")


if __name__ == "__main__":
    main()
