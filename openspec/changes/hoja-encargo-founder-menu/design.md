# Design

## Context

El proyecto Kessoku Dev es un sitio estático construido con Astro 5 y Tailwind CSS alojado en GitHub Pages (`base: '/KessokuDev'`).
Para acelerar el cierre comercial del MVP B2B y mantener la agilidad operativa de los fundadores (estudiantes de LTIN y Negocios en CUCEA), se requiere:
1. Una Hoja de Encargo B2B formal en una ruta dedicada (`/encargo`) que condense alcance, anticipo del 50%, tiempo de entrega de 5 días hábiles y firmas legales en 1 sola página imprimible/PDF.
2. Un canal de acceso encubierto (Command Palette) en el sitio web para que los fundadores abran documentos y herramientas internas sin exponer menús privados al público.

## Goals / Non-Goals

**Goals:**
- Crear la página `src/pages/encargo.astro` con diseño de documento ejecutivo técnico, optimizada con CSS `@media print` para caber exactamente en una hoja tamaño Carta (Letter) sin desbordes.
- Incluir botón flotante de exportación que invoque `window.print()` (Guardar como PDF) y desaparezca durante la impresión.
- Permitir interactividad ligera en pantalla: campos de fecha, cliente y selección de paquete marcables antes de imprimir.
- Crear el componente `src/components/FounderPalette.astro` integrado en `src/layouts/Layout.astro`.
- Implementar listener de teclado global (`Cmd+K` en macOS, `Ctrl+K` en Windows/Linux) con `e.preventDefault()` y tecla `Escape` para cerrar.
- Implementar disparador táctil en dispositivos móviles mediante triple toque en el isotipo `KD` (`Header.astro`) en menos de 600 ms.
- Garantizar compatibilidad absoluta con `import.meta.env.BASE_URL` para que todas las rutas funcionen tanto en desarrollo local como en GitHub Pages.

**Non-Goals:**
- No implementar sistemas de autenticación por servidor o bases de datos (se trata de herramientas de acceso rápido en frontend estático).
- No generar contratos multi-página (la regla comercial es 1 sola hoja de encargo cerrada).
- No utilizar librerías externas pesadas (como `jsPDF` o `html2canvas`) para evitar distorsión tipográfica y sobrepeso en el bundle; se utiliza la capacidad vectorial nativa de los navegadores mediante `@media print`.

## Decisions

### Decisión 1: Impresión Vectorial Nativa con `@media print` vs. Librerías JS de PDF
- **Elección**: CSS `@media print` + `window.print()`.
- **Racional**: Genera PDFs con texto vectorial real, nítido y seleccionable a 300+ DPI sin añadir peso a la aplicación (0 KB de dependencias JS adicionales).
- **Alternativas descartadas**:
  - `html2pdf.js` / `jspdf`: Renderizan lienzos rasterizados borrosos, fallan con fuentes web modernas y añaden más de 150 KB al bundle.

### Decisión 2: Disparadores de la Paleta de Fundadores (Cmd+K + Triple-Tap)
- **Elección**: Atajo dual: `Cmd+K` / `Ctrl+K` en teclado físico para laptops, y un contador de toques (triple-tap en `< 600ms`) en el elemento del logo `#brand-badge` para smartphones.
- **Racional**: En una reunión presencial en CUCEA o frente a un cliente, el cofundador de negocios o técnico puede pulsar rápidamente 3 veces el logo en su teléfono y abrir la hoja de encargo al instante sin que el cliente note menús sospechosos de desarrollador.
- **Alternativas descartadas**:
  - Enlace discreto en el footer: Expuesto a indexación de rastreadores y visible si el cliente revisa el pie de página.
  - Parámetro URL `?admin=true`: Incómodo de teclear en móviles durante una reunión comercial.

### Decisión 3: Arquitectura de la Hoja de Encargo (Strict 1-Page Constraint)
- **Elección**: Estructura de rejilla compacta de 4 secciones principales con altura delimitada:
  1. Header corporativo (Logo Kessoku Dev, Folio KD-2026-XXXX, Fecha, Plazo 5 días hábiles).
  2. Datos del Cliente & Alcance (Razón social, RFC/ID, Encargado, Casillas de verificación para P01, P02, P03 y Add-ons).
  3. Términos y Condiciones Esenciales (50% anticipo, entrega en 5 días, exclusión de software fuera de catálogo, soporte de 30 días, CLABE interbancaria).
  4. Bloque de Firmas Duales (Línea de firma y sello de conformidad para Cliente y Kessoku Dev).
- **Racional**: La psicología del comprador PyME valora la inmediatez y la falta de "letra chiquita" confusa. 1 página formal transmite certeza y rapidez.

### Decisión 4: Manejo de Rutas Base en Astro
- **Elección**: Uso estricto de `${import.meta.env.BASE_URL.replace(/\/$/, '')}/encargo` en todos los enlaces y scripts.
- **Racional**: Previene enlaces rotos (404) al desplegar en GitHub Pages bajo `/KessokuDev/`.

## Risks / Trade-offs

- **[Riesgo]**: Desborde a página 2 al imprimir en navegadores con configuraciones de márgenes dispares (ej. Safari vs Chrome).
  - **Mitigación**: Configurar `@page { size: letter portrait; margin: 8mm 10mm; }`, fijar tamaños de fuente relativos compactos (`text-[9px]` a `text-xs`), aplicar `page-break-inside: avoid` en los bloques y eliminar cabeceras y pies de página automáticos del navegador con CSS.
- **[Riesgo]**: Interferencia del atajo `Cmd+K` con el buscador predeterminado del navegador.
  - **Mitigación**: Ejecutar `e.preventDefault()` inmediatamente al detectar la pulsación de la combinación de teclas.
