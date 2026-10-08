# Spec Delta

## Purpose

Provee un sistema integral de apariencia visual dual (Modo Claro predeterminado y Modo Oscuro conmutable) con persistencia en el navegador y prevención total de parpadeo (FOUC).

## ADDED Requirements

### Requirement: Modo Claro como Tema Predeterminado
El sistema SHALL inicializar la interfaz en Modo Claro por defecto para todos los visitantes que no cuenten con una preferencia guardada previa en `localStorage`.

#### Scenario: Primera visita al sitio sin configuración previa
- **WHEN** un usuario accede por primera vez a cualquier ruta de la web
- **THEN** el elemento `html` adopta la clase `light` y renderiza el fondo en papel técnico claro (`#f8fafc`) con tipografía oscura de alto contraste (`#090d16`).

#### Scenario: Contraste de acentos en modo claro
- **WHEN** el sitio está en Modo Claro
- **THEN** los componentes visuales (insignias, botones, tarjetas) muestran bordes tenues bien definidos (`#e2e8f0`) y sombras suaves sin perder identidad gráfica técnica.

### Requirement: Conmutación Instantánea de Tema
El sistema SHALL proveer un control táctil e interactivo en la barra de navegación superior que permita alternar instantáneamente entre Modo Claro y Modo Oscuro mediante un solo clic.

#### Scenario: Transición de Modo Claro a Modo Oscuro
- **WHEN** el usuario hace clic en el conmutador de tema estando en Modo Claro
- **THEN** el sistema añade la clase `dark` al elemento `html`, retira la clase `light`, actualiza el icono interactivo (Sol/Luna) y almacena `dark` en `localStorage`.

#### Scenario: Transición de Modo Oscuro a Modo Claro
- **WHEN** el usuario hace clic en el conmutador de tema estando en Modo Oscuro
- **THEN** el sistema añade la clase `light` al elemento `html`, retira la clase `dark`, actualiza el icono interactivo y almacena `light` en `localStorage`.

### Requirement: Prevención de Parpadeo de Carga (Anti-FOUC)
El sistema SHALL ejecutar un script síncrono y bloqueante en la cabecera `<head>` de la página antes del pintado del DOM para aplicar la clase de tema sin saltos visuales o destellos de color.

#### Scenario: Carga con preferencia oscura almacenada
- **WHEN** un usuario con preferencia previa `dark` recarga la página o navega a otra sección
- **THEN** el script en `<head>` aplica inmediatamente `class="dark"` antes de renderizar los elementos, garantizando 0 ms de parpadeo de color.

### Requirement: Persistencia en Almacenamiento Local
El sistema SHALL guardar la preferencia de tema bajo la clave `kd-theme` en el almacenamiento local del cliente (`localStorage`) y sincronizar el estado visual entre pestañas.

#### Scenario: Navegación entre vistas del sitio
- **WHEN** el usuario conmuta el tema a Modo Oscuro y luego navega hacia `/encargo` o vuelve al inicio
- **THEN** la preferencia se mantiene intacta en la nueva página sin requerir interacción adicional.
