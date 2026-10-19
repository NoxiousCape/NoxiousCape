"""Captura fotogramas del banner animado en puntos de tiempo concretos.

Inserta el SVG en línea en una página, pausa todas las animaciones CSS en el
momento indicado y hace una captura. Es una herramienta de desarrollo para
revisar la animación paso a paso; no forma parte del repo publicado.

Uso:
    python scripts/preview_animation.py [salida.html]
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import ASSETS  # noqa: E402

TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>body{{margin:0;background:#0d1117}}</style></head>
<body>
{svg}
<script>
requestAnimationFrame(() => {{
  const t = {time};
  document.getAnimations().forEach(a => {{
    try {{ a.pause(); a.currentTime = t; }} catch (e) {{}}
  }});
  document.title = 'ready';
}});
</script>
</body></html>
"""


def main() -> None:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("preview.html")
    times = [0, 500, 1200, 2000, 3200]

    svg_path = sorted(ASSETS.glob("banner-dark.v*.svg"))[-1]
    svg = svg_path.read_text(encoding="utf-8")
    svg = svg.replace("<svg ", "<svg style='display:block' ", 1)

    for time in times:
        html = TEMPLATE.format(svg=svg, time=time)
        target = output.with_name(f"{output.stem}-{time}{output.suffix}")
        target.write_text(html, encoding="utf-8")
        print(target)


if __name__ == "__main__":
    main()
