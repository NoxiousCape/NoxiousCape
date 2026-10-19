# Assets del perfil

Los gráficos del README (**banner**, **radar**, **tarjetas de métricas**,
**lenguajes** e **iconos del stack**) no son imágenes hechas a mano: se
**generan con código** a partir de archivos de datos en JSON. Así el perfil se
puede actualizar sin abrir un editor de imágenes.

```
assets/
├── banner.json        # contenido del banner (terminal)
├── skills.json        # ejes y valores del radar
├── stats.json         # tarjetas de métricas
├── languages.json     # volumen de código por lenguaje
├── stack.json         # lista de iconos del stack técnico
├── version.json       # versión de los assets (para romper la caché)
└── state.json         # huellas del contenido de la última generación
```

## Regenerar

```bash
python scripts/generate.py
```

El script:

1. regenera los SVG con la versión actual,
2. calcula la **huella SHA-256** de cada asset,
3. la compara con `assets/state.json`,
4. si el contenido cambió, **sube la versión** (`v1` → `v2`), regenera, borra
   los SVG de versiones anteriores y reescribe las referencias del README,
5. si nada cambió, no toca nada.

Comparar por huella y no por "el archivo es igual que en disco" importa: si
editas un script y ejecutas **sólo** ese script, el disco ya coincide con lo
generado, pero el README seguiría apuntando a un archivo con el mismo nombre
y GitHub no refrescaría la caché. Con `state.json` el caso se detecta igual.

```bash
python scripts/generate.py --bump   # fuerza el cambio de versión
```

### El stack de iconos se descarga aparte

`assets/stack.svg` viene de **skillicons.dev** (logotipos de simple-icons,
MIT/CC0). Se **auto-hospeda** en vez de enlazarse al CDN: el README no debe
depender de un servicio externo que puede caerse. Para actualizarlo:

```bash
python scripts/fetch_stack.py
```

La lista de iconos se edita en `assets/stack.json`. Este archivo **no** lleva
versión en el nombre porque lo actualiza una persona, no el workflow.

### Por qué el número de versión en el nombre del archivo

GitHub cachea los SVG embebidos en un README durante **semanas**. Si el
archivo se llama siempre `banner-dark.svg`, el cambio no se ve hasta que la
caché expira. Al incluir la versión en el nombre (`banner-dark.v1.svg`), la
URL cambia y el navegador pide el archivo nuevo.

`scripts/sync_readme.py` mantiene el README apuntando a la versión vigente.

## Scripts

| Archivo | Qué genera |
|---|---|
| `scripts/svgkit.py` | Utilidades compartidas: paletas, temas, helpers de SVG |
| `scripts/banner.py` | `banner-{dark,light}.svg` — la terminal animada con el perfil |
| `scripts/radar.py` | `radar-{dark,light}.svg` — radar de habilidades |
| `scripts/cards.py` | `card-stats-{dark,light}.svg` — tarjetas de métricas |
| `scripts/languages.py` | `metrics.languages-{dark,light}.svg` — volumen por lenguaje |
| `scripts/fetch_stack.py` | Descarga `stack.svg` desde skillicons.dev |
| `scripts/sync_readme.py` | Alinea el README con la versión de los assets |
| `scripts/generate.py` | Ejecuta todo lo anterior |
| `scripts/preview_animation.py` | **Herramienta de desarrollo**: genera páginas que pausan la animación del banner en un instante concreto, para revisar el efecto paso a paso |

Cada script se puede ejecutar por separado.

## El banner animado

El banner es una terminal SVG con tres animaciones CSS, sin JavaScript:

| Animación | Qué hace |
|---|---|
| **Máquina de escribir** | Cada línea se revela de izquierda a derecha con un `clipPath` que se ensancha; las líneas aparecen en cascada |
| **Cursor** | El bloque al final de la última línea parpadea indefinidamente |
| **Brillo** | Una franja de luz recorre la barra de acento superior |

### Degradar con elegancia

Si el navegador **no ejecuta** las animaciones —porque el usuario pidió menos
movimiento, porque el motor no soporta `width` animado en SVG, o porque el
saneador de GitHub elimina el `<style>`— el banner se ve **completo y
estático**, nunca vacío.

La técnica: el atributo `width` del `<rect>` del recorte es siempre el ancho
final de la línea, y la animación va de `0px` a ese valor con
`animation-fill-mode: backwards`. Sin animación, manda el atributo.

> El ritmo se ajusta en las constantes de `scripts/banner.py`:
> `TYPE_DURATION`, `TYPE_STAGGER`, `CURSOR_BLINK` y `SHINE_DURATION`.

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
sólo si algo cambió de verdad. `stack.svg` queda fuera del workflow: requiere
descargar de skillicons.dev y se actualiza a mano.

## Restricciones al escribir SVG

Para que GitHub los renderice sin romperlos:

* **No** usar `<filter>`, `<foreignObject>` ni `<script>` — el saneador los elimina.
* **No** confiar en la conservación de espacios: el parser XML colapsa los
  espacios al inicio y al final de un `<text>`. En el banner cada palabra se
  dibuja como un `<text>` propio con su posición calculada.
* **Sí** usar `<title>` y `<desc>`: son el texto alternativo que GitHub
  muestra cuando la imagen no carga.
* **Las animaciones CSS sí se pueden usar**, siempre que el estado sin
  animación sea el estado final y completo.

