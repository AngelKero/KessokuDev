# Tasks

## 1. Configuración de Tokens y Estilos Globales (CSS & Tailwind)

- [x] 1.1 Configurar variables semánticas de color para Modo Claro (por defecto) y Modo Oscuro en `src/styles/global.css` junto con la directiva `@custom-variant dark`. Verificar en build local.
- [x] 1.2 Implementar script síncrono anti-FOUC en `<head>` de `src/layouts/Layout.astro` para leer `kd-theme` y aplicar clase `dark` o `light` antes del primer renderizado. Verificar ausencia de destello en carga.

## 2. Componente Conmutador de Tema (ThemeToggle)

- [x] 2.1 Crear el componente `src/components/ThemeToggle.astro` con botón accesible, iconos SVG de Sol/Luna y micro-animación de transición. Verificar renderizado del componente.
- [x] 2.2 Implementar la interactividad del conmutador: alternar clase `.dark`, guardar preferencia en `localStorage` (`kd-theme`) y emitir evento global. Verificar alternancia al hacer clic.
- [x] 2.3 Integrar `ThemeToggle.astro` en la barra de navegación superior de `src/components/Header.astro`. Verificar visualización y alineación responsiva.

## 3. Adaptación Cromática Impecable de la Landing

- [x] 3.1 Adaptar la barra de estado superior y la cabecera (`Header.astro`) para mostrar superficie nítida en Modo Claro y oscura en Modo Oscuro. Verificar contraste en ambos modos.
- [x] 3.2 Adaptar las secciones principales de `src/pages/index.astro` (Hero, Servicios, Garantías, Paquetes, CUCEA y Diagnóstico) para fondos claros de alta legibilidad con tipografía oscura profunda y sombras sutiles. Verificar legibilidad diurna.
- [x] 3.3 Adaptar el pie de página (`Footer.astro`) y la paleta de fundador (`FounderPalette.astro`) para asegurar armonía cromática y legibilidad impecable en ambos temas. Verificar contraste.

## 4. Verificación Visual y Validación

- [x] 4.1 Ejecutar `npm run build` para asegurar compilación limpia sin errores de estilos o TypeScript.
- [x] 4.2 Probar con navegador la carga inicial en Modo Claro por defecto, la conmutación a Modo Oscuro con el botón, la persistencia en `localStorage` tras recargar y la ausencia de FOUC.
- [x] 4.3 Capturar capturas de pantalla de ambos modos para validar el estándar de diseño Impeccable (jerarquía visual, contraste y nitidez).
