# founder-navigation-menu Specification

## Purpose
Provee un menú instrumental encubierto tipo Command Palette accesible exclusivamente mediante atajos o gestos táctiles para fundadores y equipo comercial.

## Requirements

### Requirement: Invocación de Menú por Atajo de Teclado
El sistema SHALL escuchar globalmente eventos de teclado y desplegar el modal de navegación interna al detectar la combinación `Cmd+K` (en macOS) o `Ctrl+K` (en Windows/Linux).

#### Scenario: Apertura mediante atajo de teclado
- **WHEN** el usuario presiona `Cmd+K` o `Ctrl+K` en cualquier página del sitio
- **THEN** el sistema abre la paleta de comandos interna y enfoca su contenedor interactivo sin provocar saltos bruscos de scroll.

#### Scenario: Cierre del modal
- **WHEN** el modal está abierto y el usuario presiona la tecla `Escape` o hace clic en el fondo semitransparente
- **THEN** el modal se cierra y restaura el estado visual previo de la página.

### Requirement: Disparador Táctil Alternativo en Dispositivos Móviles
El sistema SHALL permitir la apertura de la paleta interna en dispositivos móviles o táctiles mediante un gesto discreto de triple pulsación (triple-tap en menos de 600ms) sobre el isotipo `KD` del encabezado.

#### Scenario: Apertura por triple pulsación táctil
- **WHEN** un usuario realiza 3 toques consecutivos y rápidos sobre el badge `KD` en el header
- **THEN** el sistema abre la paleta de comandos de fundador en pantalla completa o drawer adaptable.

### Requirement: Directorio de Enlaces e Instrumental Interno
El sistema SHALL desplegar un menú instrumental organizado con accesos directos numéricos o de teclado a la Hoja de Encargo (`/encargo`), el Master Plan MVP 2026, el informe del Ecosistema CUCEA, el repositorio GitHub y canal directo de WhatsApp.

#### Scenario: Acceso directo a la Hoja de Encargo
- **WHEN** el usuario selecciona el acceso directo de Hoja de Encargo en la paleta
- **THEN** el navegador navega inmediatamente a `/encargo`.

#### Scenario: Consulta de documentación interna y repo
- **WHEN** el usuario selecciona los enlaces de documentación estratégica o repositorio
- **THEN** el sistema abre el recurso correspondiente en una nueva pestaña o visor adecuado.

### Requirement: Privacidad Visual en la Navegación Pública
El sistema SHALL garantizar que la barra de navegación pública (`Header.astro`) y el pie de página (`Footer.astro`) no muestren hipervínculos visuales ordinarios a las rutas internas o al menú de fundador.

#### Scenario: Inspección de navegación para clientes regulares
- **WHEN** un visitante común navega por el sitio público
- **THEN** la navegación visible contiene únicamente los enlaces públicos estándar (Servicios, Paquetes, Proceso, Preguntas y WhatsApp comercial).
