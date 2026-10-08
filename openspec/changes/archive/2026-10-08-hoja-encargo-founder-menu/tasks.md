# Tasks

## 1. Arquitectura de Navegación Oculta (FounderPalette)

- [x] 1.1 Crear el componente `src/components/FounderPalette.astro` con modal minimalista/técnico, lista de enlaces internos (`/encargo`, Master Plan, Reporte CUCEA, GitHub, WhatsApp) y gestión de foco accesible. Verificar que el componente renderice sin errores.
- [x] 1.2 Implementar lógica de teclado (`Cmd+K` / `Ctrl+K` para abrir, `Escape` para cerrar) con prevención de comportamiento predeterminado en `src/components/FounderPalette.astro`. Verificar que el evento abra y cierre el modal.
- [x] 1.3 Modificar `src/components/Header.astro` para adjuntar disparador táctil (triple toque en `<600ms`) en el isotipo `KD`. Verificar que 3 toques rápidos emitan el evento para abrir el modal.
- [x] 1.4 Integrar `FounderPalette.astro` en `src/layouts/Layout.astro` garantizando que esté disponible en todas las vistas del sitio con prefijo `${import.meta.env.BASE_URL}`. Verificar en build local.

## 2. Hoja de Encargo B2B de 1 Página (`/encargo`)

- [x] 2.1 Crear la ruta `src/pages/encargo.astro` con estructura de documento ejecutivo: cabecera con folio, fecha, datos de la empresa cliente y contacto comercial. Verificar visualización en navegador.
- [x] 2.2 Maquetar la sección de desglose de paquetes cerrados (P01 $7,500, P02 $12,500, P03 $18,500) y casillas de add-ons con precios claros y cálculo total visual. Verificar legibilidad y formato.
- [x] 2.3 Redactar y maquetar las cláusulas contractuales vinculantes (garantía de entrega de 5 días hábiles, 50% de anticipo, exclusión de desarrollos fuera de catálogo, datos de transferencia bancaria con CLABE). Verificar texto comercial.
- [x] 2.4 Incorporar el bloque de formalización con líneas para firma dual (Cliente y Kessoku Dev) con nombres y cargos. Verificar alineación y proporción visual.
- [x] 2.5 Añadir barra de acción flotante en pantalla con botón "Imprimir / Guardar PDF" (`window.print()`) y enlace de retorno. Verificar interactividad en pantalla.

## 3. Optimización Estricta de Impresión y PDF (`@media print`)

- [x] 3.1 Configurar reglas de estilo `@media print` y `@page { size: letter; margin: 8mm 10mm; }` en `src/pages/encargo.astro` forzando texto de alto contraste e inhabilitando fondos oscuros. Verificar en emulación de medios de impresión.
- [x] 3.2 Ocultar todos los elementos de navegación digital (barra flotante, encabezados web) en modo de impresión (`display: none !important`). Verificar que la vista de impresión esté libre de chrome web.
- [x] 3.3 Calibrar espaciados y tipografía con `page-break-inside: avoid` para asegurar que el documento completo encaje estrictamente en 1 sola hoja de papel Carta/A4 sin desborde a la página 2. Verificar vista previa de impresión en navegador.

## 4. Verificación Integral y Despliegue

- [x] 4.1 Ejecutar `npm run build` para asegurar compilación estática limpia de Astro en `dist/` sin advertencias de rutas rotas.
- [x] 4.2 Probar el flujo completo en navegador: activación mediante `Cmd+K`, apertura en móvil por triple toque en el logo `KD`, navegación hacia `/encargo` y disparo de `window.print()`.
- [x] 4.3 Validar que la navegación pública de la landing principal (`/`) permanezca completamente limpia sin enlaces visibles de las herramientas de fundador.
