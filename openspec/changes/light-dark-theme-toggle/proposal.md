# Proposal

## Why

Para maximizar la legibilidad y la confianza comercial de dueños de PyMEs tradicionales en Jalisco que revisan la propuesta bajo luz diurna o en pantallas de oficina, la plataforma necesita operar con un Modo Claro corporativo y nítido por defecto, manteniendo al mismo tiempo un Modo Oscuro técnico y de alta fidelidad para desarrolladores y evaluadores, con persistencia y sin parpadeo (FOUC).

## What Changes

- **Sistema de Temas Dual (Claro por Defecto + Oscuro)**:
  - Adopción de Modo Claro como estado inicial por defecto (`light`), con fondos tipo papel técnico blanco marfil (`#f8fafc` / `#ffffff`), tipografía de alto contraste azul marino profundo (`#090d16` / `#0f172a`), bordes sutiles y acentos cromáticos nítidos (Cobalto `#1d4ed8`, Ocre `#d97706`, Esmeralda `#059669`).
  - Preservación y adaptación del Modo Oscuro existente (`dark`), configurable a través de variables de diseño y clases contextuales en Tailwind CSS.
- **Componente Conmutador de Tema (`ThemeToggle.astro`)**:
  - Botón táctil e interactivo en la barra de navegación superior (`Header.astro`) y en el menú móvil, con micro-animación de transición entre Sol (Modo Claro) y Luna (Modo Oscuro).
  - Integración del atajo de tema en la Consola de Fundador (`FounderPalette.astro`).
- **Prevención de Parpadeo (Anti-FOUC Script)**:
  - Script bloqueante ultra-ligero en el `<head>` de `Layout.astro` que lee `localStorage.getItem('kd-theme') || 'light'` y aplica inmediatamente la clase correspondiente antes del primer renderizado gráfico.
- **Persistencia en Almacenamiento Local**:
  - Almacena la preferencia del visitante en `localStorage` bajo la clave `kd-theme` para mantener su elección entre recargas y navegación interna.

## Capabilities

### New Capabilities

- `theme-appearance-system`: Gestión integral del aspecto visual (Modo Claro predeterminado y Modo Oscuro conmutable), persistencia en el cliente, prevención de parpadeo de tema y conmutador accesible con micro-interacciones.

### Modified Capabilities

*(Ninguna capacidad funcional previa modifica sus requerimientos centrales; `landing-commercial-copy`, `order-sheet-contract` y `founder-navigation-menu` continúan operando con sus alcances definidos).*

## Impact

- **Archivos afectados**:
  - `src/styles/global.css`: Definición de variables semánticas de tema para modo claro y modo oscuro, respetando clases de Tailwind CSS.
  - `src/layouts/Layout.astro`: Inyección de script anti-FOUC en `<head>` y tokens globales.
  - `src/components/Header.astro`: Integración del nuevo componente conmutador `ThemeToggle.astro`.
  - `src/components/ThemeToggle.astro`: Nuevo componente de interruptor accesible.
  - `src/pages/index.astro` y secciones asociadas: Ajuste de contrastes y paleta cromática adaptativa.
  - `src/components/FounderPalette.astro`: Accesibilidad visual garantizada en ambos modos.
