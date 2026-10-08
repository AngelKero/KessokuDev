# Spec Delta

## Purpose

Permite generar, visualizar y exportar a PDF o imprimir una Hoja de Encargo de Servicios Tecnológicos de 1 página estricta para formalizar acuerdos B2B de entrega rápida.

## ADDED Requirements

### Requirement: Renderizado de Hoja de Encargo B2B de 1 página
El sistema SHALL renderizar en la ruta `/encargo` una Hoja de Encargo comercial estructurada que contenga folio, fecha, datos del cliente, desglose de paquetes cerrados, add-ons seleccionables y espacio de firmas dentro de un contenedor calibrado para 1 sola página.

#### Scenario: Visualización del documento en navegador
- **WHEN** un usuario navega a la ruta `/encargo`
- **THEN** el sistema muestra la Hoja de Encargo con diseño corporativo limpio, tipografía monoespaciada/sans técnica y todos los campos comerciales editables o prellenados.

#### Scenario: Contención vertical estricta
- **WHEN** se renderiza la vista de la hoja de encargo en viewport de escritorio
- **THEN** la estructura completa del documento se mantiene compacta y cohesionada para evitar desbordes de página física.

### Requirement: Exportación e Impresión Optimizada (@media print)
El sistema SHALL incluir reglas `@media print` y un botón de acción en pantalla que ejecute `window.print()`, formateando el documento a tamaño Carta/A4 en fondo blanco puro, eliminando márgenes de navegador y ocultando controles web.

#### Scenario: Ejecución de exportación / impresión
- **WHEN** el usuario presiona el botón "Imprimir / Guardar PDF"
- **THEN** el sistema invoca el diálogo de impresión del navegador (`window.print()`).

#### Scenario: Ocultamiento de elementos no imprimibles
- **WHEN** se activa el modo de impresión o exportación a PDF
- **THEN** el sistema oculta el botón flotante, la barra de navegación del sitio y cualquier elemento interactivo irrelevante para el papel.

#### Scenario: Ajuste estricto a una sola hoja física
- **WHEN** el diálogo de impresión genera la vista preliminar en formato Carta o A4
- **THEN** el documento cabe exactamente en 1 sola hoja sin generar páginas en blanco o renglones huérfanos en la página 2.

### Requirement: Cláusulas y Términos Comerciales Vinculantes
El sistema SHALL mostrar de manera destacada las condiciones comerciales estándar: entrega garantizada en 5 días hábiles, anticipo obligatorio del 50%, datos bancarios de transferencia (CLABE) y cláusula de exclusión expresa de desarrollo a medida fuera de catálogo.

#### Scenario: Visualización de cláusulas operativas
- **WHEN** se examina la sección de términos y condiciones de la Hoja de Encargo
- **THEN** se visualizan claramente el plazo de 5 días hábiles a partir de la entrega de activos y la regla de no inclusión de módulos a medida no especificados.

#### Scenario: Términos financieros y anticipo
- **WHEN** se revisan las condiciones de pago
- **THEN** el documento estipula 50% de anticipo para iniciar labores y 50% contra entrega final, junto con la clave bancaria estandarizada (CLABE).

### Requirement: Bloque de Formalización y Firmas Duales
El sistema SHALL proveer dos espacios de firma con líneas de rúbrica, nombre, cargo y fecha para la representación legal de la PyME cliente y el representante de Kessoku Dev.

#### Scenario: Presencia de rúbricas legales
- **WHEN** se visualiza el pie de la Hoja de Encargo
- **THEN** se presentan dos recuadros equilibrados para la firma del Cliente y la firma de Kessoku Dev.
