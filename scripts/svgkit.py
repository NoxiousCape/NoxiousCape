"""Utilidades compartidas para generar los SVG del perfil de GitHub.

Diseño deliberado: **solo biblioteca estándar de Python**. No requiere NumPy,
Pillow ni ningún paquete externo, así que los scripts corren en cualquier
máquina con Python 3.10+ y en GitHub Actions sin `pip install`.

Los SVG se generan con un XML plano y sin `<filter>` ni `foreignObject`,
porque el saneador de GitHub los elimina al renderizar un README.
"""

from __future__ import annotations

import html
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

# La consola de Windows suele usar cp1252: forzamos UTF-8 con reemplazo para
# que imprimir "✓" no rompa la ejecución.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
VERSION_FILE = ASSETS / "version.json"


def current_version() -> int:
    """Versión actual de los assets.

    GitHub cachea los SVG embebidos en un README durante largos periodos. Al
    subir una versión nueva hay que cambiar el nombre del archivo (``v1`` ->
    ``v2``) para que el navegador la pida de nuevo. La versión vive en
    ``assets/version.json`` y ``scripts/sync_readme.py`` la propaga al README.
    """
    if not VERSION_FILE.exists():
        return 1
    with VERSION_FILE.open(encoding="utf-8") as handle:
        return int(json.load(handle).get("version", 1))


def asset_name(base: str, theme_name: str) -> str:
    """Nombre versionado de un asset: ``banner-dark.v1.svg``."""
    return f"{base}-{theme_name}.v{current_version()}.svg"

# ------------------------------------------------------------------ paleta --


@dataclass(frozen=True)
class Theme:
    """Paleta de un tema (oscuro o claro)."""

    name: str
    bg: str
    surface: str
    border: str
    text: str
    muted: str
    accent: str
    accent2: str
    accent3: str
    accent4: str
    grid: str
    titlebar: str

    def color(self, key: str) -> str:
        """Resuelve un nombre de color (``accent``, ``accent2``...)."""
        return getattr(self, key)


DARK = Theme(
    name="dark",
    bg="#0d1117",
    surface="#161b22",
    border="#30363d",
    text="#e6edf3",
    muted="#8b949e",
    accent="#3fb950",
    accent2="#58a6ff",
    accent3="#f0883e",
    accent4="#bc8cff",
    grid="#21262d",
    titlebar="#1c2128",
)

LIGHT = Theme(
    name="light",
    bg="#ffffff",
    surface="#f6f8fa",
    border="#d0d7de",
    text="#1f2328",
    muted="#59636e",
    accent="#1a7f37",
    accent2="#0969da",
    accent3="#bc4c00",
    accent4="#8250df",
    grid="#eaeef2",
    titlebar="#eaeef2",
)

THEMES = {"dark": DARK, "light": LIGHT}

MONO = "'JetBrains Mono','Fira Code','Cascadia Code',Consolas,'DejaVu Sans Mono',monospace"
SANS = "'Inter','Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,sans-serif"

# ------------------------------------------------------------------ helpers --


def esc(text: Any) -> str:
    """Escapa texto para insertarlo como contenido XML."""
    return html.escape(str(text), quote=True)


def load_json(filename: str) -> Any:
    """Carga un JSON desde ``assets/``.

    Se lee con ``utf-8-sig`` a propósito: las herramientas de Windows
    (PowerShell 5.1, Bloc de notas) guardan los archivos con BOM, que con
    ``utf-8`` estricto hace fallar el parser. ``utf-8-sig`` acepta los dos
    casos.
    """
    path = ASSETS / filename
    if not path.exists():
        raise FileNotFoundError(f"Falta el archivo de datos: {path}")
    with path.open(encoding="utf-8-sig") as handle:
        return json.load(handle)


def save_svg(base: str, width: int, height: int, body: str, theme: Theme,
             title: str, desc: str = "") -> Path:
    """Envuelve un cuerpo SVG y lo escribe en ``assets/``.

    El nombre incluye la versión (``banner-dark.v1.svg``) para poder romper la
    caché del navegador desde GitHub.

    Se añaden ``<title>`` y ``<desc>`` para que el SVG sea legible por
    lectores de pantalla, algo que GitHub respeta en las imágenes.
    """
    path = ASSETS / asset_name(base, theme.name)
    path.parent.mkdir(parents=True, exist_ok=True)
    uid = theme.name
    header = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-labelledby="t-{uid} d-{uid}">'
        f"<title id=\"t-{uid}\">{esc(title)}</title>"
        f"<desc id=\"d-{uid}\">{esc(desc or title)}</desc>"
    )
    # newline="\n" es obligatorio: sin él, Windows traduce los saltos de
    # línea a CRLF y el archivo queda un byte distinto al que genera Linux.
    # Como la detección de cambios se hace por huella SHA-256, esa diferencia
    # haría que el workflow de GitHub Actions regenerase los assets —y
    # subiese la versión— en cada ejecución.
    path.write_text(f"{header}{body}</svg>\n", encoding="utf-8", newline="\n")
    return path


def text(x: float, y: float, content: str, *, size: int = 14, weight: int = 400,
         fill: str = "#000", anchor: str = "start", family: str = SANS,
         opacity: float | None = None, letter_spacing: float | None = None,
         cls: str | None = None) -> str:
    """Emite un ``<text>`` con una línea de texto posicionada.

    Cada fragmento se dibuja como un ``<text>`` independiente con su propio
    ``x``: así no dependemos de la conservación de espacios en blanco, que
    el renderizador de GitHub no garantiza.
    """
    attrs = [
        f'x="{fmt(x)}"', f'y="{fmt(y)}"', f'font-family="{family}"',
        f'font-size="{size}"', f'fill="{fill}"',
    ]
    if weight != 400:
        attrs.append(f'font-weight="{weight}"')
    if anchor != "start":
        attrs.append(f'text-anchor="{anchor}"')
    if opacity is not None:
        attrs.append(f'opacity="{fmt(opacity)}"')
    if letter_spacing is not None:
        attrs.append(f'letter-spacing="{fmt(letter_spacing)}"')
    if cls:
        attrs.append(f'class="{cls}"')
    return f"<text {' '.join(attrs)}>{esc(content)}</text>"


def rect(x: float, y: float, w: float, h: float, *, fill: str = "none",
         stroke: str | None = None, rx: float = 0, ry: float | None = None,
         stroke_width: float = 1, opacity: float | None = None,
         cls: str | None = None) -> str:
    """Emite un ``<rect>``."""
    attrs = [f'x="{fmt(x)}"', f'y="{fmt(y)}"', f'width="{fmt(w)}"', f'height="{fmt(h)}"']
    attrs.append(f'rx="{fmt(rx)}"')
    attrs.append(f'ry="{fmt(rx if ry is None else ry)}"')
    attrs.append(f'fill="{fill}"')
    if stroke:
        attrs.append(f'stroke="{stroke}"')
        attrs.append(f'stroke-width="{fmt(stroke_width)}"')
    if opacity is not None:
        attrs.append(f'opacity="{fmt(opacity)}"')
    if cls:
        attrs.append(f'class="{cls}"')
    return f"<rect {' '.join(attrs)}/>"


def circle(cx: float, cy: float, r: float, *, fill: str = "none",
           stroke: str | None = None, stroke_width: float = 1,
           opacity: float | None = None) -> str:
    """Emite un ``<circle>``."""
    attrs = [f'cx="{fmt(cx)}"', f'cy="{fmt(cy)}"', f'r="{fmt(r)}"', f'fill="{fill}"']
    if stroke:
        attrs.append(f'stroke="{stroke}"')
        attrs.append(f'stroke-width="{fmt(stroke_width)}"')
    if opacity is not None:
        attrs.append(f'opacity="{fmt(opacity)}"')
    return f"<circle {' '.join(attrs)}/>"


def line(x1: float, y1: float, x2: float, y2: float, *, stroke: str,
         stroke_width: float = 1, opacity: float | None = None,
         dash: str | None = None, cap: str = "round") -> str:
    """Emite una ``<line>``."""
    attrs = [f'x1="{fmt(x1)}"', f'y1="{fmt(y1)}"', f'x2="{fmt(x2)}"', f'y2="{fmt(y2)}"',
             f'stroke="{stroke}"', f'stroke-width="{fmt(stroke_width)}"',
             f'stroke-linecap="{cap}"']
    if opacity is not None:
        attrs.append(f'opacity="{fmt(opacity)}"')
    if dash:
        attrs.append(f'stroke-dasharray="{dash}"')
    return f"<line {' '.join(attrs)}/>"


def polygon(points: Iterable[tuple[float, float]], *, fill: str = "none",
            stroke: str | None = None, stroke_width: float = 2,
            opacity: float | None = None) -> str:
    """Emite un ``<polygon>`` a partir de pares ``(x, y)``."""
    pts = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in points)
    attrs = [f'points="{pts}"', f'fill="{fill}"']
    if stroke:
        attrs.append(f'stroke="{stroke}"')
        attrs.append(f'stroke-width="{fmt(stroke_width)}"')
        attrs.append('stroke-linejoin="round"')
    if opacity is not None:
        attrs.append(f'opacity="{fmt(opacity)}"')
    return f"<polygon {' '.join(attrs)}/>"


def gradient(identifier: str, stops: list[tuple[float, str, float]],
             *, x1: float = 0, y1: float = 0, x2: float = 1, y2: float = 0) -> str:
    """Emite un ``<linearGradient>`` dentro de ``<defs>``."""
    parts = [
        f'<linearGradient id="{esc(identifier)}" x1="{fmt(x1)}" y1="{fmt(y1)}" '
        f'x2="{fmt(x2)}" y2="{fmt(y2)}">'
    ]
    for offset, color, opacity in stops:
        parts.append(
            f'<stop offset="{fmt(offset)}" stop-color="{color}" stop-opacity="{fmt(opacity)}"/>'
        )
    parts.append("</linearGradient>")
    return "".join(parts)


def fmt(value: float) -> str:
    """Formatea un número sin ceros sobrantes (``.0`` final)."""
    if isinstance(value, int):
        return str(value)
    rounded = round(float(value), 2)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:g}"


def plural(count: int, singular: str, plural_form: str) -> str:
    """``plural(1, "proyecto", "proyectos")`` -> ``"1 proyecto"``."""
    return f"{count} {singular if count == 1 else plural_form}"
