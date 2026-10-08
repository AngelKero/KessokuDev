# Design

## Context

Actualmente, Kessoku Dev cuenta con un diseño base nocturno/cyberpunk en Tailwind v4 y Astro 5 (`bg-[#080d1a]`, `text-[#f8fafc]`). Para elevar el impacto comercial ante directores y dueños de PyMEs de Jalisco que operan en entornos diurnos y de oficina, se requiere implementar un Modo Claro de alta fidelidad como apariencia por defecto, manteniendo el Modo Oscuro disponible mediante un selector interactivo.

## Goals / Non-Goals

**Goals:**
- Establecer el Modo Claro como la experiencia predeterminada (`default: 'light'`).
- Diseñar una paleta clara editorial y técnica (Impeccable craft): fondo papel técnico `#f8fafc`, tarjetas blancas `#ffffff`, tipografía carbón ejecutivo `#090d16`, bordes limpios `#e2e8f0` y acentos contrastados (Cobalto `#1d4ed8`, Ocre `#b45309`, Esmeralda `#047857`).
- Preservar el Modo Oscuro existente (`dark`), refinando contrastes y acentos.
- Crear el componente `src/components/ThemeToggle.astro` e integrarlo en el `Header.astro`.
- Garantizar cero parpadeo visual (0ms FOUC) mediante script síncrono bloqueante en el `<head>` de `Layout.astro`.
- Persistir la selección del usuario en `localStorage` con la clave `kd-theme`.

**Non-Goals:**
- No depender de librerías externas de temas; solución 100% nativa y ligera (<1 KB JS).
- No alterar la Hoja de Encargo (`/encargo`), la cual ya cuenta con su propio motor de contraste estricto e impresión en papel blanco.

## Decisions

### Decisión 1: Estrategia de Tokens Semánticos + Tailwind v4 `@custom-variant dark`
- **Elección**: Combinar variables semánticas CSS (`--bg-page`, `--bg-surface`, `--text-primary`, `--border-ui`) con la directiva `@custom-variant dark (&:where(.dark, .dark *));` de Tailwind v4.
- **Racional**: Permite que el selector `.dark` controle tanto las variables globales de fondo/texto como las clases utilitarias de Tailwind en componentes existentes sin necesidad de reescribir todo el HTML.
- **Alternativas descartadas**:
  - `prefers-color-scheme` puro: No permite al usuario forzar el tema explícitamente independientemente de su sistema operativo.

### Decisión 2: Script Anti-FOUC Inline en `<head>`
- **Elección**: Script mínimo bloqueante colocado antes de la carga de estilos y scripts diferidos:
  ```html
  <script is:inline>
    const savedTheme = localStorage.getItem('kd-theme') || 'light';
    if (savedTheme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  </script>
  ```
- **Racional**: Garantiza que el navegador conozca la clase antes del primer layout/paint, eliminando cualquier destello blanco o negro durante la carga.

### Decisión 3: Diseño del Conmutador (`ThemeToggle.astro`)
- **Elección**: Botón táctil compacto ubicado en el Header con iconos vectoriales de Sol y Luna con transición CSS fluida (`rotate`, `scale`, `opacity`).
- **Racional**: Proporciona feedback táctil inmediato y cumple con estándares de accesibilidad (botón nativo con `aria-label`).

## Risks / Trade-offs

- **[Riesgo]**: Elementos con colores hexadecimales fijos (`bg-[#080d1a]`) que no respondan al cambio de tema.
  - **Mitigación**: Sustituir selectores fijos críticos en la landing por variables semánticas o clases duales `bg-slate-50 dark:bg-[#080d1a]` y `text-slate-900 dark:text-[#f8fafc]`.
- **[Riesgo]**: Contraste insuficiente de textos secundarios en Modo Claro.
  - **Mitigación**: Seguir los lineamientos de la habilidad Impeccable: asegurar un ratio de contraste mínimo de 4.5:1 para texto normal utilizando Slate-600 (`#475569`) o Slate-700 (`#334155`) en lugar de grises pálidos.
