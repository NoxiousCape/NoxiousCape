"""Descarga los iconos del stack técnico desde skillicons.dev.

Los iconos se **auto-hospedan** en ``assets/stack.svg`` en vez de enlazarse al
CDN de skillicons.dev. Motivo: el README no debe depender de un servicio
externo que puede caerse; con el archivo en el repo, los iconos siempre están
ahí y además se versionan con el resto del perfil.

La lista de iconos se edita en ``assets/stack.json``.

Uso:
    python scripts/fetch_stack.py
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from svgkit import ASSETS  # noqa: E402

# Los logotipos de skillicons.dev provienen de simple-icons (MIT/CC0).
ATTRIBUTION = (
    "Iconos generados con skillicons.dev a partir de los logotipos de "
    "simple-icons (MIT / CC0)."
)

USER_AGENT = "Mozilla/5.0 (compatible; noxiouscape-profile/1.0)"


def build_url(config: dict) -> str:
    """Construye la URL de skillicons.dev a partir de la configuración."""
    params = {
        "i": config["icons"],
        "perline": str(config.get("perline", 9)),
    }
    if config.get("theme") and config["theme"] != "original":
        params["theme"] = config["theme"]
    return "https://skillicons.dev/icons?" + urllib.parse.urlencode(params)


def download(url: str) -> str:
    """Descarga el SVG y lo devuelve como texto."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def normalize(svg: str) -> str:
    """Limpia el SVG servido: quita el espacio de nombres `xlink`, fija un
    tamaño intrínseco legible (el original trae decimales odd) y normaliza los
    saltos de línea a LF para que el archivo sea idéntico en cualquier
    sistema."""
    svg = svg.replace(' xmlns:xlink="http://www.w3.org/1999/xlink"', "")
    svg = svg.replace(' version="1.1"', "")
    svg = svg.replace("\r\n", "\n").replace("\r", "\n")
    return svg.strip()


def main() -> None:
    config_path = ASSETS / "stack.json"
    with config_path.open(encoding="utf-8-sig") as handle:
        config = json.load(handle)

    url = build_url(config)
    print(f"Descargando {url}")

    try:
        svg = normalize(download(url))
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"  ✗ No se pudo descargar: {error}")
        print("    Se conserva el archivo anterior.")
        raise SystemExit(1) from error

    if "<svg" not in svg:
        print("  ✗ La respuesta no parece un SVG válido.")
        raise SystemExit(1)

    output = ASSETS / config.get("output", "stack.svg")
    output.write_text(svg + "\n", encoding="utf-8", newline="\n")

    icons = len(config["icons"].split(","))
    size_kb = output.stat().st_size / 1024
    print(f"  ✓ {output.name}  ({icons} iconos, {size_kb:.1f} KB)")
    print(f"    {ATTRIBUTION}")


if __name__ == "__main__":
    main()
