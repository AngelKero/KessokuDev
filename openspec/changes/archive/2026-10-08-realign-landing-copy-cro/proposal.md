# Proposal

## Why

El contenido actual de la landing page sufrió de la "trampa de la metáfora de IA" y la "maldición del conocimiento": adoptó una analogía literal de despacho aduanal y comercio exterior ("Partida arancelaria", "Waybill", "Docks clear", "Zarpar") que resulta incomprensible para el cliente objetivo real identificado en la investigación de CUCEA (dueños de PyMEs locales y directores de negocios tradicionales de Guadalajara).

Esta desconexión cognitiva destruye la tasa de conversión en los primeros 5 segundos, haciendo que el sitio parezca una agencia aduanal del puerto de Manzanillo en lugar de una firma de desarrollo web de alto rendimiento con precios transparentes y sede universitaria. Es urgente reescribir todo el contenido aplicando las disciplinas de `landing-page-cro`, `humanizer`, `impeccable clarify` y `landing-page-optimizer` para hablarle directamente al comprador en lenguaje humano, claro y comercial.

## What Changes

- **Purgado total de la metáfora de IA:** Se eliminan todas las referencias ficticias a trámites aduanales, fletes y partidas arancelarias.
- **Reescritura del Hero y First Viewport (Test de los 5 Segundos):** El titular (H1), subtítulo y llamados a la acción responden de forma inmediata y literal: qué es (sitios web de calidad internacional), para quién es (PyMEs y negocios en crecimiento), por qué creer (respaldo de CUCEA y métricas reales) y qué hacer después (diagnóstico gratuito de 15 min).
- **Traducción de Telemetría a Beneficios Tangibles:** Los 6 diales técnicos dejan de medir métricas abstractas de aviónica y pasan a certificar los compromisos reales que le importan a la PyME: velocidad móvil (< 1s), indexación en Google Maps, canal directo a WhatsApp, entrega en 5 días y cero costos ocultos.
- **Presentación Clara de Paquetes Cerrados:** Los paquetes ($7.5k, $12.5k, $18.5k) se presentan como soluciones llave en mano sin jerga de "contenedores", manteniendo la regla inquebrantable de "cero desarrollos a la medida desordenados".
- **Alineación con la Ruta de Vinculación CUCEA:** Se posiciona explícitamente a Kessoku Dev como el brazo técnico que ejecuta la programación que el Hospital PyME e IDITpyme no realizan, ubicando la sede en la Torre Smart Campus (Piso 2).
- **Formulario de Conversión sin Fricción:** Formulario directo para agendar la "Auditoría Digital de 15 min" en campus o videollamada.

## Capabilities

### New Capabilities
- `landing-commercial-copy`: Arquitectura de mensajes comerciales, propuesta de valor above-the-fold, presentación de paquetes accesibles para PyMEs y ruta de conversión formal sin jerga interna.

### Modified Capabilities
<!-- Ninguna capacidad previa existe en el repositorio -->

## Impact

- **Componentes modificados:**
  - `src/components/Header.astro`
  - `src/components/Hero.astro`
  - `src/components/TelemetryDials.astro`
  - `src/components/WaybillPackages.astro`
  - `src/components/CuceaTerminal.astro`
  - `src/components/AuditSection.astro`
  - `src/components/Footer.astro`
- **Documentación de diseño:** Actualización de `DESIGN.md` para reflejar la voz comercial humana y la verdad del producto sin alterar los tokens visuales ni el rendimiento de 60fps.
