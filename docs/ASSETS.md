# Assets del perfil

Los gráficos del README (**banner**, **radar**, **tarjetas de métricas** y
**lenguajes**) no son imágenes hechas a mano: se **generan con código** a partir
de archivos de datos en JSON. Así el perfil se puede actualizar sin abrir un
editor de imágenes.

```
assets/
├── banner.json        # contenido del banner (terminal)
├── skills.json        # ejes y valores del radar
├── stats.json         # tarjetas de métricas
├── languages.json     # volumen de código por lenguaje
└── version.json       # versión de los assets (para romper la caché)
```

## Regenerar

```bash
python scripts/generate.py
```

El script:

1. regenera los SVG con la versión actual,
2. **compara** el resultado con lo que ya estaba en el disco,
3. si el contenido cambió, **sube la versión** (`v1` → `v2`) y reescribe las
   referencias del README,
4. borra los SVG de versiones anteriores.

Si nada cambió, no se toca nada: así el workflow de GitHub Actions no genera
commits de ruido.

```bash
python scripts/generate.py --bump   # fuerza el cambio de versión
```

### Por qué el número de versión en el nombre del archivo

GitHub cachea los SVG embebidos en un README durante **semanas**. Si el
archivo se llama siempre `banner-dark.svg`, el cambio no se ve hasta que la
caché expira. Al incluir la versión en el nombre (`banner-dark.v1.svg`), la
URL cambia y el navegador pide el archivo nuevo.

`scripts/sync_readme.py` mantiene el README apuntando a la versión vigente.

## Scripts

| Archivo | Qué genera |
|---|---|
| `scripts/svgkit.py` | Utilidades compartidas: paletas, paletas de tema, helpers de SVG |
| `scripts/banner.py` | `banner-{dark,light}.svg` — la terminal con el perfil |
| `scripts/radar.py` | `radar-{dark,light}.svg` — radar de habilidades |
| `scripts/cards.py` | `card-stats-{dark,light}.svg` — tarjetas de métricas |
| `scripts/languages.py` | `metrics.languages-{dark,light}.svg` — volumen por lenguaje |
| `scripts/sync_readme.py` | Alinea el README con la versión de los assets |
| `scripts/generate.py` | Ejecuta todo lo anterior |

Cada script se puede ejecutar por separado.

## Temas

`svgkit.py` define dos paletas (`DARK` y `LIGHT`). El README los selecciona con
`<picture>` y `prefers-color-scheme`, de modo que el gráfico se adapta al tema
del sistema sin necesidad de generar dos archivos a mano:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/radar-dark.v1.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/radar-light.v1.svg">
  <img alt="…" src="assets/radar-dark.v1.svg" width="620">
</picture>
```

## Automatización

`.github/workflows/assets.yml` regenera los assets cada lunes y sube el commit
sólo si algo cambió de verdad.

## Restricciones al escribir SVG

Para que GitHub los renderice sin romperlos:

* **No** usar `<filter>`, `<foreignObject>` ni `<script>` — el saneador los elimina.
* **No** confiar en la conservación de espacios: el parser XML colapsa los
  espacios al inicio y al final de un `<text>`. En el banner cada palabra se
  dibuja como un `<text>` propio con su posición calculada.
* **Sí** usar `<title>` y `<desc>`: son el texto alternativo que GitHub
  muestra cuando la imagen no carga.
