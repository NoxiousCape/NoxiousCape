<div align="center">

# Hola, soy Daniel 👋

**Ingeniero de Software · Full Stack · Automatización · IA aplicada**

Construyo software que convierte **procesos complejos y reales** en herramientas
confiables, usables y mantenibles *fuera* del entorno de desarrollo.

[![GitHub](https://img.shields.io/badge/GitHub-NoxiousCape-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NoxiousCape)
[![Portfolio](https://img.shields.io/badge/Portfolio-mydtravels.com-0A66C2?style=for-the-badge)](https://mydtravels.com/)
[![Email](https://img.shields.io/badge/Email-danielpaezzamudio0@hotmail.com-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:danielpaezzamudio0@hotmail.com)
[![X](https://img.shields.io/badge/X-@NoxiousCape-000000?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/NoxiousCape)
[![Instagram](https://img.shields.io/badge/Instagram-noxiouscape-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/noxiouscape/)

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.v6.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.v6.svg">
  <img alt="Terminal con el perfil, el stack técnico y el resumen del portafolio de Daniel Páez" src="assets/banner-dark.v6.svg" width="100%">
</picture>

---

<a id="indice"></a>

## 🧭 Índice

[Sobre mí](#sobre-mi) · [Una mirada](#mirada) · [Trabajo seleccionado](#trabajo) ·
[Repos públicos](#repos) · [Perfil técnico](#perfil) · [Experiencia](#experiencia) ·
[Contacto](#contacto)

---

<a id="mirada"></a>

<a id="sobre-mi"></a>

## 🧑‍💻 Sobre mí

Soy **Daniel Steven Páez Zamudio**, ingeniero de Sistemas y Computación de la
**Universidad Pedagógica y Tecnológica de Colombia (UPTC)**, en Sogamoso, Boyacá.

Trabajo sobre todo donde un proceso manual, repetitivo y dependiente de
terceros se puede convertir en **software que aguanta la operación real**:
automatización de portales públicos, sistemas de consulta judicial, herramientas
de escritorio que se instalan con un doble clic e integraciones que sobreviven
a que el servicio externo falle.

```text
✦  Full Stack Web      ·  Aplicaciones de escritorio    ·  IA y LLM
✦  Automatización      ·  Procesamiento de datos        ·  APIs e integraciones
✦  Despliegue en nube  ·  Arquitectura y diseño técnico ·  Datos a escala
```

---

## 🖼️ Una mirada

Todo esto es software funcionando, no maquetas. Estas son las seis piezas que
mejor resumen el portafolio; el resto aparece en las fichas de abajo.

<table>
  <tr>
    <td width="33%" align="center" valign="top">
      <img src="assets/shots/secop.v3.webp" alt="Dashboard de Procesos SECOP: 56 procesos con detalle verificado, estado del portal en línea y los módulos de búsqueda" width="100%">
      <br><b>SECOP Optimizado</b><br><sub>Escritorio · La Manuelina</sub>
    </td>
    <td width="33%" align="center" valign="top">
      <img src="assets/shots/central.v3.webp" alt="Pantalla de búsqueda SAMAI de Central de Consultas La Manuelina, con el menú de radicado, parte procesal, Rama Judicial y consulta masiva" width="100%">
      <br><b>Central de Consultas</b><br><sub>Web · La Manuelina</sub>
    </td>
    <td width="33%" align="center" valign="top">
      <img src="assets/shots/asobancaria.v3.webp" alt="Pantalla de acceso de ASOBANCARIA con el botón Continuar con Microsoft" width="100%">
      <br><b>ASOBANCARIA</b><br><sub>Web · La Manuelina</sub>
    </td>
  </tr>
  <tr>
    <td width="33%" align="center" valign="top">
      <img src="assets/shots/pdex.v3.webp" alt="Ventana de PDEx con los cinco pasos de la conversión de Excel a PDF" width="100%">
      <br><b>PDEx</b><br><sub>Escritorio · Excel → PDF</sub>
    </td>
    <td width="33%" align="center" valign="top">
      <img src="assets/shots/abacre-debug.v3.webp" alt="OllyDbg mostrando el error 251 de protección que dispara el packer de Abacre al detectar el depurador" width="100%">
      <br><b>Abacre Antivirus</b><br><sub>Investigación · Código público</sub>
    </td>
    <td width="33%" align="center" valign="top">
      <img src="assets/shots/mydtravels.v3.webp" alt="Portada de M&D Travels con el buscador de destinos y los indicadores de destinos, viajeros y soportes" width="100%">
      <br><b>M&D Travels</b><br><sub>Web con IA · En producción</sub>
    </td>
  </tr>
</table>

---

<a id="trabajo"></a>

## 🏗️ Trabajo seleccionado

Una parte de mi portafolio es **privada o confidencial**: el código, los datos y
la infraestructura de varios de estos sistemas no pueden hacerse públicos. Aun
así, lo que construí y por qué está a la vista.

> 👆 **Abre cada proyecto** para ver el stack, los retos técnicos y cómo quedó.
>
> Cada línea lleva una etiqueta de **madurez**: 🟢 en producción · 🔬 trabajo
> documentado · 🛠️ en construcción.

> 👤 **Contribución individual.** En los sistemas comerciales de este perfil
> **diseñé la arquitectura, implementé el código y opero el despliegue**, de
> principio a fin. Los proyectos académicos de la UPTC (`SIGBMS`) se
> desarrollaron en equipo con dos compañeros.

### ⚖️ Plataformas judiciales y de contratación pública

*Trabajo comercial, en producción con usuarios reales.*

<details>
<summary><b>★ 🔎 SECOP Optimizado</b> · escritorio para consultar y seguir procesos de contratación en SECOP<br><i>🟢 En producción · La Manuelina S.A.S. · 2026 · Node.js · React · MariaDB · Playwright</i></summary>

Plataforma **de escritorio** que automatiza la consulta del portal transaccional
del Estado colombiano: 442 códigos UNSPSC, búsquedas por hora y por entidad, y
**lotes automatizados** que se pueden pausar y reanudar.

<img src="assets/shots/secop.v3.webp" alt="Dashboard de Procesos SECOP: 56 procesos con detalle verificado, el indicador del portal en línea con su latencia y los módulos de búsqueda" width="100%">

<sub>El Dashboard: procesos con detalle verificado, búsquedas registradas, procesos
seguidos y el estado real del portal con su tiempo de respuesta.</sub>

* Automatización sobre una **sesión autenticada**, con resolución humana del CAPTCHA: el flujo no salta la comprobación ni la resuelve por medios técnicos
* **Caché ≠ base de datos**: cada búsqueda en vivo nutre la base sola; repetir no re-scrapea
* Lotes **reanudables** (3 fallos → pausa, Excel con una hoja por código) y **SSE reanexable**: si se cae la conexión, el servidor retoma la misma búsqueda
* Instalador con doble clic, base propia o reutilización de un MySQL ya presente, y **actualización en un clic** con verificación SHA-256
* **452 pruebas** de Vitest más integración contra MySQL

</details>

<details>
<summary><b>★ 📚 Central de Consultas</b> · plataforma web para consultar procesos judiciales en Colombia<br><i>🟢 En producción · La Manuelina S.A.S. · 2026 · Node.js · Express · MySQL · ExcelJS · SSE</i></summary>

Consulta de procesos judiciales en dos jurisdicciones —**SAMAI** y **Rama
Judicial**— más **consulta masiva** de estados desde Excel.

<img src="assets/shots/central.v3.webp" alt="Pantalla de búsqueda SAMAI de Central de Consultas La Manuelina, con el menú de radicado, parte procesal, Rama Judicial y consulta masiva" width="100%">

<sub>Búsqueda por radicado con la corporación deducida del número, y el menú
completo: parte procesal, Rama Judicial y los tres modos de consulta masiva.</sub>

* Búsqueda por **radicado de 23 dígitos** con identificación automática de la corporación, y por parte procesal sobre un catálogo de **76 corporaciones judiciales**
* **Puente entre jurisdicciones**: los radicados no contenciosos redirigen a Rama Judicial y viceversa, con autobúsqueda en ambas
* Expediente completo, visor PDF con progreso y descarga con el nombre real
* **Consulta masiva** desde Excel: checkpoint reanudable, **soporta lotes de 142 k+ filas**, progreso SSE con ritmo y ETA, reintentos dirigidos y log de fallos por fila
* **Búsqueda ampliada** con barrido geográfico (Departamento → Ciudad → Entidad → Especialidad → Despacho) para superar el límite de 1 000 registros
* **Modo offline**: expedientes y PDFs ya consultados se sirven desde caché

</details>

<details>
<summary><b>★ 🏛️ ASOBANCARIA</b> · gestión de procesos judiciales y legislativos con identidad federada<br><i>🟢 En producción · La Manuelina S.A.S. · 2026 · Next.js · TypeScript · Prisma · MySQL · Entra ID · Railway</i></summary>

Plataforma institucional para el seguimiento de procesos judiciales
(Corte Constitucional y Consejo de Estado) y del **proceso legislativo**
(Senado, Cámara y Gacetas).

<img src="assets/shots/asobancaria.v3.webp" alt="Pantalla de acceso de ASOBANCARIA con el botón Continuar con Microsoft, sobre el logotipo institucional de La Manuelina y TRADENS" width="100%">

<sub>El acceso real a la plataforma: identidad federada de Microsoft Entra ID,
con el cierre de sesión único y los roles ya resueltos en el token.</sub>

* **Autenticación real con Microsoft Entra ID**: app registration, login federado y single sign-out
* Ingesta y **normalización de datos desde Excel** como paso formal del proyecto
* Exportación a Excel y PDF con un criterio visual único
* Despliegue en **Railway** con Dockerfile propio y add-on MySQL
* Entorno local **sin Docker**: SQLite embebido en Prisma y modo `mock` de autenticación

</details>

<details>
<summary><b>🗂️ Consulta Masiva Procuraduría</b> · escritorio para consultar nombres por lotes de cédulas<br><i>🟢 En producción · TRADENS · 2026 · Python · Playwright · NiceGUI · arquitectura hexagonal</i></summary>

Herramienta que consulta **nombres y apellidos** en la Sede Electrónica de la
Procuraduría General de la Nación a partir de un Excel de cédulas.

<img src="assets/shots/tradens.v3.webp" alt="Interfaz de Consulta Masiva Procuraduría: carga del archivo de lote en Excel, configuración de persona y documento, pausa entre consultas y reintentos" width="100%">

<sub>El flujo completo en una pantalla: cargar el lote, configurar los parámetros
de la consulta y ejecutarla con los contadores en vivo.</sub>

* **Investigación documentada**: no existe API REST pública; el portal es *low-code* Appian con reCAPTCHA Enterprise
* **Arquitectura hexagonal** (dominio / puertos / adaptadores): si mañana se contrata una API de pago, se cambia **un solo adaptador** y el negocio no se toca
* Lotes con reintentos con backoff, pausa humana, **checkpoint de reanudación** y deduplicación
* CLI **y** UI web local, distribuida como un único `.exe` portable
* Decisión documentada: portable y no en la nube, porque el reCAPTCHA penaliza las IP de datacenter

</details>

### 🧰 Herramientas de escritorio

*Software que se instala con un doble clic y trabaja sin terminal ni servidor.*

<details>
<summary><b>📄 PDEx</b> · convierte hojas Excel densas en un PDF legible, ordenado y completo<br><i>🟢 En producción · uso corporativo · Python · Tkinter · ReportLab · PyInstaller</i></summary>

Herramienta **100 % local** que convierte hojas Excel densas —cientos de filas,
celdas de hasta 32 k caracteres— en un **PDF legible, ordenado y completo**,
con maquetación inteligente en lugar de impresión directa.

<img src="assets/shots/pdex.v3.webp" alt="Ventana de PDEx con los cinco pasos de la conversión: archivo Excel, hoja, configuración de página, destino y generación del PDF" width="100%">

<sub>El asistente completo: elegir el Excel, la hoja, el papel y las márgenes, y
generar el PDF con la barra de progreso en vivo.</sub>

* **Análisis de estructura** (no simple impresión): perfil de columnas y filas, anchos dinámicos y columnas problemáticas
* Principio rector explícito: `Legibilidad > Organización > Aprovechamiento > Reducción de páginas` — **nunca** se recorta, oculta ni resume
* Fragmentación de mega-filas (> 1 página) por frontera de párrafo, con etiqueta `ID (cont. k/n)` y control viuda/huérfana
* **Validación automática**: correspondencia de IDs, páginas vacías y verificación del documento generado
* Portada opcional, salida unificada multi-hoja, alineación del texto de tabla, distribución corporativa con SemVer

</details>

<details>
<summary><b>💼 M&D Cotizaciones</b> · cotizador de viajes con navegador embebido y export a Excel y PDF<br><i>🟢 En producción · M&D Travels Colombia · Electron · ExcelJS · LaTeX · OpenRouter</i></summary>

App de escritorio para que el equipo de la agencia prepare cotizaciones
profesionales: **no busca sola**, integra un navegador donde el cotizante
navega Booking, Airbnb y aerolíneas, captura las ofertas con un clic y exporta
todo a Excel o a un PDF generado con LaTeX.

* **Navegador embebido** completo con barra de marcadores, y captura de la oferta con un solo clic (o `Alt + A`)
* Exportación a **Excel** con totales en COP y a **PDF** con LaTeX en estilo *boarding pass*
* **IA opcional** (OpenRouter) que **sólo redacta**: la búsqueda la hace una persona
* Alertas de presupuesto en vivo y **auto-actualización** vía GitHub Releases

</details>

### 🔬 Investigación e ingeniería inversa

*Trabajo propio, documentado y reproducible: se puede leer el método completo.*

<details>
<summary><b>★ 🧬 Abacre Antivirus 1.3</b> · ingeniería inversa forense de un antivirus con 0 % de detección<br><i>🔬 Documentado · código público · Python · C/C++ · VMWare · NTSD · OllyDbg</i></summary>

Análisis estático y forense de un antivirus de 2006 que obtuvo **0 % de
detección** en dos pruebas de `virus.gr` (113 334 y 147 184 muestras).

<img src="assets/shots/abacre.v3.webp" alt="Contenido extraído del instalador de Abacre Antivirus: el ejecutable, el módulo de protección y la base de datos de firmas" width="100%">

<sub>Los ocho archivos extraídos del instalador: el ejecutable empaquetado, el
módulo de protección y la base de datos de firmas, que resultó ser la pieza
central del análisis.</sub>

* **Protocolo académico estricto**: los binarios nunca se ejecutan en el host, solo en una VM aislada **sin red** (Windows XP SP3)
* El *packer* detecta a OllyDbg (`Error 251`); `NTSD -pv` permite obtener un **dump completo de 29 MB** sin activar la detección
* Hallazgo central: cifrador **Blowfish** y una base de solo **67 firmas (2003-2005)** — la explicación plausible del 0 %
* 24 capturas de debugging, scripts Python reproducibles y hashes SHA-256 de cada artefacto
* **Honestidad intelectual**: el README separa hechos de hipótesis y enumera lo que **no** se pudo verificar

<img alt="OllyDbg mostrando el error 251 de protección que dispara el packer de Abacre al detectar el depurador" src="assets/shots/abacre-debug.v3.webp" width="100%">

*El packer detecta el depurador y aborta con `Error 251`. Con `NTSD -pv` el mismo
proceso se volca completo: por eso el repositorio documenta los **dos** intentos
y no sólo el que funcionó.*

🔗 **[NoxiousCape/Abacre_Investigation](https://github.com/NoxiousCape/Abacre_Investigation)** — *el repositorio incluye las 24 capturas completas del proceso*

</details>

<details>
<summary><b>🔎 Investigación de portales sin API pública</b> · cómo se resuelve un sistema que no ofrece interfaz<br><i>🔬 Documentado · SECOP · SAMAI · Rama Judicial · Procuraduría · Curaduría</i></summary>

Parte del trabajo no es una aplicación, es **descubrir cómo funciona un sistema
que no ofrece interfaz para lo que necesito**:

| Portal | El obstáculo | La salida |
|---|---|---|
| **SECOP** | Transaccional con captcha, sin API documentada | Sesión autenticada + automatización con las reglas del portal respetadas |
| **SAMAI** | Sólo expone expediente y documentos vía sesión web | Playwright con reintentos, backoff y clasificación de errores |
| **Rama Judicial** | API JSON real, con tope de 1 000 registros | Pacer global y barrido geográfico para rodear el tope |
| **Procuraduría** | Appian *low-code* con reCAPTCHA Enterprise | Dominio propio con puerto `ProveedorConsulta` intercambiable |
| **Curaduría Urbana** | Resoluciones en PDF escaneado | Pipeline OCR con detección de la página resumen y saneado de alucinaciones |

El resultado suele acabar en un **dataset de referencia** —como los 17 457
elementos de la tabla piramidal— o en una capa de abstracción que permite
cambiar de proveedor sin reescribir el negocio.

</details>

<details>
<summary><b>🏗️ CodRamExc</b> · dataset y herramienta de los códigos de radicación de la Rama Judicial<br><i>🔬 Documentado · Python · requests · openpyxl · PyInstaller</i></summary>

Extrae la **estructura jerárquica real** de los códigos que usa la Rama Judicial
para construir el número de radicación, y la exporta como tabla piramidal
clasificada por ciudad.

<img src="assets/shots/codramexc.v3.webp" alt="Ventana del generador de estructura de radicación de la Rama Judicial, con las opciones de obtener la estructura completa, obtener una muestra o exportar a Excel" width="100%">

<sub>La herramienta: obtener la estructura nacional completa, una muestra rápida
de una ciudad, o exportar el Excel ya clasificado.</sub>

* Cobertura **nacional**: 33 departamentos, **17 457 elementos**, 11 551 rutas constructoras, reporte de inconsistencias sin observaciones
* Excel de 5 hojas: estructura jerárquica, datos normalizados, **constructor de códigos**, relaciones y reporte de calidad
* Extracción **reanudable** (caché + checkpoint) frente a 403 intermitentes y respuestas vacías: el reintento y el backoff son explícitos, nunca silenciosos
* La investigación de la fuente y la validación ejecutada están documentadas por separado (`INVESTIGACION.md`, `VALIDACION.md`)

</details>

### 🏛️ Repositorios públicos

*Código abierto: se puede leer, ejecutar y auditar.*

<a id="repos"></a>

| | Repositorio | Qué es | Stack |
|---|---|---|---|
| <img src="assets/shots/sigbms.v3.webp" alt="Catálogo de libros de SIGBMS, la Biblioteca Municipal de Sogamoso" width="120"> | **[SIGBMS](https://github.com/NoxiousCape/SIGBMS)** | Sistema integral de gestión para la Biblioteca Municipal de Sogamoso | `Java 21` `Spring Boot 3.1` `MySQL 8` |
| <img src="assets/shots/unblockex.v3.webp" alt="UnBlockEx en la pestaña de fuerza bruta, con la selección de caracteres y la longitud configurables" width="120"> | **[UnBlockEx](https://github.com/NoxiousCape/UnBlockEx)** | Recuperación de Excel cifrado (AES-256) por tres estrategias | `Python` `Tkinter` |
| | **[Abacre_Investigation](https://github.com/NoxiousCape/Abacre_Investigation)** | Ingeniería inversa forense de un antivirus histórico | `Python` `C/C++` |
| | **[La_Manuelina_Web](https://github.com/NoxiousCape/La_Manuelina_Web)** | Portal SECOP & CC2026: normalización de datos, MySQL, roles JWT y PWA offline | `Node.js` `Express` `MySQL` `PWA` |
| | **[Triki](https://github.com/NoxiousCape/Triki)** | Tres en línea: web *glassmorphism* + consola en Ruby, IA con Minimax | `JavaScript` `Ruby` |
| | **[Cadenas_en_C](https://github.com/NoxiousCape/Cadenas_en_C)** | Manipulación de cadenas con menú interactivo | `C` |

> **SIGBMS** se desarrolló para la materia *Ingeniería de Software II* de la
> **UPTC**, junto a dos compañeros y bajo la dirección del Ing. Edmundo Junco.

### 🌍 Sitios y productos para clientes

*Trabajo comercial entregado y en funcionamiento.*

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <img src="assets/shots/mydtravels.v3.webp" alt="Portada de M&D Travels con el buscador de destinos y los indicadores de destinos, viajeros y soportes" width="100%">
      <br><b>M&D Travels</b> · <a href="https://mydtravels.com/">mydtravels.com</a><br>
      <sub>Sitio con asistente de viajes con IA, blog desde RSS, PWA, reCAPTCHA y Resend</sub>
    </td>
    <td width="50%" align="center" valign="top">
      <img src="assets/shots/deleitarte.v3.webp" alt="Portada de DeleitArte Pastelería Creativa, con el catálogo de pasteles artesanales" width="100%">
      <br><b>DeleitArte</b> · <a href="https://pasteleriadeleitarte.com/">pasteleriadeleitarte.com</a><br>
      <sub>Catálogo, armador de pasteles 3D, pedido libre con foto, reserva de espacio y PWA</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <img src="assets/shots/jrmantenimiento.v3.webp" alt="Portada de JR Mantenimiento Eléctrico y Redes, con las soluciones de ingeniería eléctrica" width="100%">
      <br><b>JR Mantenimiento Eléctrico</b> · <a href="https://jrmantenimientoelectrico.com/">jrmantenimientoelectrico.com</a><br>
      <sub>Sitio corporativo con GSAP y Swiper, PWA, legal (Habeas Data) y SEO técnico</sub>
    </td>
    <td width="50%" align="center" valign="top">
      <img src="assets/shots/dupe.v3.webp" alt="Portada de Dupé Perfumería con la colección exclusiva y el acceso a la experiencia" width="100%">
      <br><b>Dupé Perfumería</b> · <a href="https://duperfumes.vercel.app/">duperfumes.vercel.app</a><br>
      <sub>E-commerce editorial con React + Vite, kiosco táctil con quiz de recomendación y PWA</sub>
    </td>
  </tr>
</table>

**La Manuelina (web institucional)** — portal con módulos de SECOP y Corte
Constitucional, control por roles y PWA offline.

---

<a id="en-desarrollo"></a>

## 🚧 En desarrollo

*Proyecto propio, en construcción: lo que viene después.*

<details>
<summary><b>🏙️ SogNow</b> · plataforma cívica para rastrear los proyectos urbanos de Sogamoso<br><i>🛠️ En construcción · proyecto propio · Python · FastAPI · PostgreSQL + PostGIS · Next.js · Leaflet</i></summary>

Centraliza, rastrea y **visualiza los proyectos urbanos** (privados y públicos)
de Sogamoso, hoy dispersos entre curaduría, secretaría, medios locales y redes
sociales.

* **Fase 1 — MVP (en ejecución):** esquema PostGIS, motor de extracción **OCR** y filtrado por impacto urbanístico (niveles, área, uso)
* **Fase 2 — Automatización:** scraping de licencias PDF de la Curaduría, detección de la página resumen del proyecto y normalización de OCR y direcciones
* **Fase 3:** alertas por zona, enriquecimiento con IA y dashboard de estadísticas urbanas

</details>

---

<a id="perfil"></a>

## 🧠 Perfil técnico

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/radar-dark.v6.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/radar-light.v6.svg">
  <img alt="Radar de habilidades: en producción y en investigación" src="assets/radar-dark.v6.svg" width="620">
</picture>

<sub>El radar **no** es una puntuación de prestigio: contrasta lo que ya está
**aplicado en producción** contra lo que está **en investigación**. La evidencia
de lo primero son los proyectos de arriba.</sub>

<div align="center">

<img alt="Stack tecnológico: TypeScript, JavaScript, React, Next.js, Node.js, Express, Python, Java, C, PostgreSQL, MySQL, Tailwind, Prisma, Electron, Docker, Git y GitHub" src="assets/stack.svg" width="720">

</div>

> 🤖 **IA aplicada, no experimentos de laboratorio.** Un recomendador que
> degrada a un *fallback* local cuando el modelo no responde; un redactor que
> **sólo redacta y jamás busca** (la búsqueda la hace una persona, con
> criterio); y un pipeline OCR con detección de la página resumen y saneado de
> alucinaciones sobre documentos escaneados. En los tres casos, la IA es una
> pieza dentro de un sistema que tiene que funcionar sin ella.

| Todo el portafolio (público + privado) | Solo repos públicos (medido por la API) |
|---|---|
| <picture><source media="(prefers-color-scheme: dark)" srcset="assets/metrics.languages-dark.v6.svg"><source media="(prefers-color-scheme: light)" srcset="assets/metrics.languages-light.v6.svg"><img alt="Lenguajes por volumen de código en todos los proyectos" src="assets/metrics.languages-dark.v6.svg" width="100%"></picture> | <img alt="Lenguajes más usados en los repositorios públicos" src="profile/top-langs.svg" width="300"> |

<sub>La columna izquierda suma los repos públicos (medidos con la API de GitHub) y
los proyectos privados (estimados a partir de su estructura). La derecha es la
métrica estándar de GitHub, sin estimaciones.</sub>

<details>
<summary><b>Ver el stack por capas</b></summary>

| Capa | Tecnologías |
|---|---|
| **Lenguajes** | `TypeScript` · `JavaScript` · `Python` · `Java` · `C#` · `C` / `C++` |
| **Frontend** | `React` · `Next.js` · `HTML5` · `CSS3` · `Tailwind CSS` · `Three.js` · `GSAP` |
| **Backend** | `Node.js` · `Express` · `Spring Boot` · `REST APIs` · `SSE` |
| **Escritorio** | `Electron` · `Python (Tkinter / NiceGUI)` · `PyInstaller` · `Inno Setup` |
| **Datos** | `MySQL` · `PostgreSQL + PostGIS` · `SQLite` · `Excel` · `LaTeX` |
| **Automatización** | `Playwright` · `OCR (Tesseract)` · `n8n` · `OpenRouter` · `Gemini API` |
| **Despliegue** | `Git` · `GitHub Actions` · `Docker` · `Railway` · `Vercel` · `Azure` |
| **Otros** | `Unity` · `QGIS` · `ROS` |

</details>

---

<a id="experiencia"></a>

## 💼 Experiencia profesional

**🏢 Full Stack Developer — La Manuelina S.A.S.** *(Septiembre 2026 — actualidad)*
Desarrollo de soluciones para requisitos operativos e institucionales: plataformas
web full stack · arquitectura y diseño técnico · integraciones de autenticación
e identidad · diseño de bases de datos · APIs · ingesta y procesamiento de
datos · automatización y herramientas internas · infraestructura de nube ·
integración con sistemas externos.

**✈️ Software Engineer & Co-Founder — M&D Travels Colombia**
Construcción de la infraestructura digital de la empresa: plataformas web,
software interno, automatización y herramientas asistidas por IA.

**🎮 Unity Programming Instructor — Kodland**
Enseñanza de programación y desarrollo de juegos con **C# y Unity**.

---

## 🔒 Trabajo comercial y confidencial

No todo mi trabajo puede hacerse público. Varios de los sistemas que desarrollo
están destinados a **empresas, operaciones internas e entornos institucionales**,
donde el código, los datos y la infraestructura no pueden exponerse.

Incluso con el repositorio en privado, sí puedo explicar la ingeniería detrás
del proyecto: arquitectura, integraciones de API, diseño de base de datos,
autenticación e identidad, procesamiento de datos, estrategias de
automatización, caché y resiliencia, infraestructura de despliegue, flujos de
trabajo, consideraciones de rendimiento y los desafíos técnicos con sus
soluciones.

> **Construir software que tiene que funcionar más allá del entorno de desarrollo
> es una parte importante de mi experiencia.**

---

<a id="contacto"></a>

## 📫 Contacto

[![Email](https://img.shields.io/badge/Email-danielpaezzamudio0@hotmail.com-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:danielpaezzamudio0@hotmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-NoxiousCape-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NoxiousCape)
[![X](https://img.shields.io/badge/X-@NoxiousCape-000000?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/NoxiousCape)
[![Instagram](https://img.shields.io/badge/Instagram-noxiouscape-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/noxiouscape/)
[![Facebook](https://img.shields.io/badge/Facebook-danielsteven.paezzamudio-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/danielsteven.paezzamudio)

Si tienes un proceso manual, repetitivo o dependiente de un tercero que te
gasta horas al mes, probablemente se pueda automatizar. **Escríbeme.**

---

<div align="center">

<sub>Hecho con ☕ en Sogamoso, Boyacá — Colombia 🇨🇴</sub>

</div>
