# Tasks

## 1. Header y Cintillo Institucional

- [x] 1.1 Reemplazar el cintillo portuario por el ticker institucional de CUCEA (cupos de auditoría semanal, respaldo universitario y estado operativo) en `src/components/Header.astro` y verificar que no queden referencias a fletes ni aduanas.
- [x] 1.2 Ajustar los enlaces de navegación (`01/ Servicios`, `02/ Garantías`, `03/ Paquetes`, `04/ Sede CUCEA`) y el botón principal (`Diagnóstico $0`) en `src/components/Header.astro` y comprobar legibilidad en pantalla.

## 2. Hero y First Viewport (Prueba de los 5 Segundos)

- [x] 2.1 Reescribir el titular H1 y subtítulo en `src/components/Hero.astro` con la fórmula de resultado sin dolor ("Tu negocio en internet con calidad de gran empresa. En 5 días y a precio accesible para tu PyME").
- [x] 2.2 Reemplazar la hoja de inspección aduanal por la "Ficha de Garantía de Servicio Kessoku Dev / CUCEA" con sellos de garantía universitaria y firmas fundadoras en `src/components/Hero.astro`.
- [x] 2.3 Actualizar los llamados a la acción primario y secundario con verbos orientados a valor ("Solicitar Diagnóstico Web $0", "Ver Paquetes y Precios") en `src/components/Hero.astro`.

## 3. Consola de Compromisos y Garantías Técnicas

- [x] 3.1 Traducir los 6 diales técnicos de `src/components/TelemetryDials.astro` hacia beneficios medibles para el dueño de PyME (velocidad móvil < 1s, indexación en Google Maps, canal de WhatsApp, entrega en 5 días, sin costos ocultos, soporte mensual).
- [x] 3.2 Verificar que las barras de progreso, badges de estado y descripciones en `src/components/TelemetryDials.astro` reflejen compromisos comerciales sin perder la estética instrumental.

## 4. Catálogo de Paquetes Cerrados y Add-ons

- [x] 4.1 Actualizar los nombres, alcances y listas de verificación de los 3 paquetes en `src/components/WaybillPackages.astro` (Paquete 01: Presencia Digital $7.5k, Paquete 02: Catálogo & Cotizador WhatsApp $12.5k, Paquete 03: Plataforma Comercial & Expansión $18.5k).
- [x] 4.2 Reestructurar los add-ons cerrados (Sheets Sync $1,800, Citas Google Calendar $2,200, Pasarela de Pago $3,500) reafirmando la política de cero desarrollos a la medida desordenados en `src/components/WaybillPackages.astro`.

## 5. Ruta Institucional CUCEA y Comparativa de Mercado

- [x] 5.1 Redactar la narrativa del "puente de implementación" en `src/components/CuceaTerminal.astro`, explicando cómo Kessoku Dev resuelve la programación técnica que Hospital PyME e IDITpyme no cubren.
- [x] 5.2 Confirmar la sede física en Torre Smart Campus (Piso 2) y Módulo P, y verificar que la tabla comparativa contraste los costos frente a agencias tradicionales ($80k-$250k MXN).

## 6. Formulario de Captura de Prospectos

- [x] 6.1 Simplificar el formulario en `src/components/AuditSection.astro` enfocándolo en agendar la sesión de diagnóstico de 15 minutos (presencial en CUCEA o por videollamada) con cupo semanal limitado.
- [x] 6.2 Verificar el mensaje de confirmación y feedback visual al enviar el formulario en `src/components/AuditSection.astro`.

## 7. Footer y Actualización de Documentación de Diseño

- [x] 7.1 Actualizar el acta de cierre en `src/components/Footer.astro` con la misión universitaria, roles de los fundadores (LTIN + LINI) y sede en Zapopan.
- [x] 7.2 Actualizar `DESIGN.md` para asentar la nueva voz comercial humana y la verdad de producto libre de metáforas crípticas.

## 8. Verificación y Auditoría CRO Integral

- [x] 8.1 Ejecutar `npm run build` para garantizar cero errores de compilación estática.
- [x] 8.2 Ejecutar `.gemini/skills/impeccable/scripts/impeccable detect src/` para validar 0 anti-patrones de diseño.
- [x] 8.3 Capturar screenshot con Chrome headless y verificar la aprobación de los 3 arquetipos de comprador bajo el skill `landing-page-cro`.
