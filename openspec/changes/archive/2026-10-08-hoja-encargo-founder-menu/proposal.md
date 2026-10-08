# Proposal

## Why

Para cerrar ventas B2B presenciales en CUCEA y PyMEs de Guadalajara, el equipo comercial necesita un documento físico/PDF vinculante e inmediato (Hoja de Encargo de 1 sola página) que formalice el alcance cerrado, el anticipo del 50% y los 5 días hábiles de entrega sin dispersión ni redacción de contratos artesanales de 10 páginas.
Al mismo tiempo, los fundadores necesitan acceder rápidamente en sus dispositivos móviles y laptops a herramientas internas (la Hoja de Encargo, reportes estratégicos, demos futuras y repositorios) a través de un menú o paleta de comandos privada integrada en el sitio de Astro, sin ensuciar la navegación pública de los clientes.

## What Changes

- **Página de Hoja de Encargo B2B (`/encargo`)**: Creación de una ruta dedicada en Astro diseñada para visualización web y exportación impecable a PDF mediante `@media print` en exactamente 1 página tamaño Carta/A4. Incluye folio, datos del cliente, selección de paquetes cerrados (P01 $7.5k, P02 $12.5k, P03 $18.5k) y add-ons, términos comerciales estrictos (50% anticipo, 5 días de entrega, exclusión de software a la medida fuera de catálogo), datos de transferencia CLABE y espacio de firmas duales (Cliente y Kessoku Dev).
- **Botón de Acción de Impresión / Exportación a PDF**: Botón flotante en pantalla (`Imprimir / Guardar PDF`) que invoca `window.print()` y desaparece automáticamente en la vista de impresión.
- **Paleta de Comandos / Menú Oculto de Fundadores (`FounderPalette`)**: Componente global discreto accesible mediante atajo de teclado (`Cmd+K` / `Ctrl+K`) en desktop o triple toque en el badge/isotipo de Kessoku Dev (`KD`) en móviles/tablets.
- **Accesos Directos del Menú de Fundador**:
  - `[01]` Hoja de Encargo B2B (`/encargo`)
  - `[02]` Master Plan Estratégico 2026 (descarga/lectura del plan MVP en PDF o Markdown)
  - `[03]` Reporte de Ecosistema CUCEA (acceso a la investigación de vinculación)
  - `[04]` Repositorio y Despliegue GitHub (enlace al repo oficial)
  - `[05]` Acceso directo a contacto comercial de emergencia / WhatsApp del equipo

## Capabilities

### New Capabilities

- `order-sheet-contract`: Generación, renderizado y exportación a PDF de la Hoja de Encargo de Servicios Tecnológicos de 1 página, optimizada para impresión física y formalización inmediata de ventas B2B.
- `founder-navigation-menu`: Sistema de navegación encubierto tipo Command Palette accesible exclusivamente mediante atajo de teclado (`Cmd+K` / `Ctrl+K`) o gesto en el logotipo, permitiendo el acceso rápido a enlaces internos y utilidades de fundador sin exponerlos en el menú público.

### Modified Capabilities

*(Ninguna capacidad existente modifica sus requisitos funcionales; `landing-commercial-copy` se preserva intacta).*

## Impact

- **Rutas afectadas**: Nueva página `src/pages/encargo.astro`.
- **Componentes**: Nuevo componente `src/components/FounderPalette.astro` integrado en `src/layouts/Layout.astro` para disponibilidad en todo el sitio. Modificación en `src/components/Header.astro` para adjuntar el disparador de gesto táctil en el isotipo `KD`.
- **Estilos / CSS**: Reglas de `@media print` dedicadas para formato Carta estricto a 1 sola página, ocultamiento de elementos no imprimibles (header, footer, botones flotantes) y forzado de fondos claros legibles para impresión física.
- **Dependencias**: Cero dependencias npm adicionales requeridas; utiliza Vanilla JS nativo para el modal/drawer de atajos y eventos del DOM.
