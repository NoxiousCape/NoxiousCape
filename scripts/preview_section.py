"""Renderiza un fragmento del README para revisar cómo queda.

Herramienta de desarrollo; no forma parte del repositorio publicado.

Uso:
    python scripts/preview_section.py "## 🖼️ Una mirada" [salida.html]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import ROOT  # noqa: E402

TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-light.min.css">
<style>body{{margin:0;background:#fff}}.markdown-body{{max-width:1012px;margin:0 auto;padding:24px}}</style>
</head><body><article class="markdown-body" id="out"></article>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script>
const md = {markdown};
document.getElementById('out').innerHTML = marked.parse(md);
</script></body></html>
"""


def main() -> None:
    start_marker = sys.argv[1] if len(sys.argv) > 1 else "## 🖼️ Una mirada"
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "section.html"

    text = (ROOT / "README.md").read_text(encoding="utf-8")
    start = text.find(start_marker)
    if start < 0:
        print(f"No se encontró {start_marker!r}")
        return

    # Corta hasta el siguiente encabezado de nivel 2.
    rest = text[start:]
    match = re.search(r"\n## ", rest[1:])
    fragment = rest[: match.start() + 1] if match else rest

    # Las rutas de los assets son relativas al README: desde otra carpeta
    # no resuelven, así que se convierten a absolutas para el preview.
    base = ROOT.as_uri()
    fragment = fragment.replace('src="assets/', f'src="{base}/assets/')

    output.write_text(
        TEMPLATE.format(markdown=json.dumps(fragment)),
        encoding="utf-8",
    )
    print(output)


if __name__ == "__main__":
    main()
