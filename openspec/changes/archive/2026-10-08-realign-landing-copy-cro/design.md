# Design

## Context

El proyecto cuenta con una implementación funcional en Astro 5, Tailwind CSS v4, GSAP y Lenis con 0 errores de detección en Impeccable (ver `proposal.md`). Sin embargo, el contenido de texto actual presenta una severa desconexión comercial debido a la adopción literal de jerga aduanal. Este diseño define cómo reestructurar los mensajes en cada componente manteniendo intacta la infraestructura técnica y el rendimiento visual de 60fps.

## Goals / Non-Goals

**Goals:**
- Alinear el contenido al 100% con los hallazgos de `REPORTE_ECOSISTEMA_CUCEA_KESSOKU_DEV.md` y `ONE_PAGER_KESSOKU_DEV.md`.
- Implementar las recomendaciones de `landing-page-cro`, `humanizer`, `impeccable clarify` y `landing-page-optimizer`.
- Superar el test de los 5 segundos para que cualquier dueño de PyME de Guadalajara entienda el valor en su primera lectura.
- Preservar el rendimiento técnico (Core Web Vitals, 60fps, WCAG AA).

**Non-Goals:**
- No se modifica la arquitectura técnica (Astro, Tailwind, GSAP).
- No se añaden formularios complejos de múltiples pasos ni pasarelas de pago backend en esta fase.
- No se inventan clientes ficticios ni testimonios fabricados.

## Decisions

### Decisión 1: Reescritura del Hero con la fórmula "Resultado deseado sin el dolor común"
- **Elección:** Titular H1: *"Tu negocio en internet con calidad de gran empresa. En 5 días y a precio accesible para tu PyME"*.
- **Razón:** Ataca el dolor principal descubierto en CUCEA: las PyMEs temen a las agencias que cobran $80,000–$250,000 MXN y tardan 2 meses, o a freelancers que dejan trabajos rotos.
- **Alternativa descartada:** Mantener el eslogan abstracto *"Cero aranceles por desorden"*.

### Decisión 2: Reinterpretación de la consola de 6 diales hacia compromisos tangibles
- **Elección:** Mantener la cuadrícula de 6 diales visuales pero midiendo compromisos orientados al cliente:
  1. Carga móvil ultra-rápida (< 1s)
  2. Indexación y presencia en Google Maps
  3. Canal directo de cotización por WhatsApp
  4. Tiempo récord de entrega (5 a 7 días hábiles)
  5. Cero costos ocultos de hosting y dominio
  6. Soporte continuo y mantenimiento mensual
- **Razón:** Comunica rigor técnico sin alienar al comprador no técnico.

### Decisión 3: Catálogo de paquetes con nombres funcionales directos
- **Elección:**
  - Paquete 01: *Presencia Digital & Google Maps* ($7,500 MXN)
  - Paquete 02: *Catálogo & Cotizador WhatsApp* ($12,500 MXN - Recomendado)
  - Paquete 03: *Plataforma Comercial & Expansión* ($18,500 MXN)
- **Razón:** Permite al cliente auto-identificarse inmediatamente con su etapa de negocio.

### Decisión 4: Purgado de sintaxis sintética mediante Humanizer
- **Elección:** Redacción en español mexicano profesional, directo, sin fórmulas corporativas de relleno ("en el vertiginoso mundo digital", "un testimonio de innovación").
- **Razón:** Genera cercanía, credibilidad y postura de socios de negocio confiables.

## Risks / Trade-offs

- **[Riesgo de perder sofisticación visual al simplificar el vocabulario]** → *Mitigación:* Se preservan los contenedores de alta densidad, la tipografía Chivo/Public Sans/Azeret Mono y los badges interactivos; solo se vuelve transparente el mensaje.
- **[Riesgo de saturación en solicitudes de auditoría gratuita]** → *Mitigación:* Se establece un cupo semanal visible ("Cupo limitado: 4 auditorías por semana") que gestiona la capacidad y añade urgencia legítima.
