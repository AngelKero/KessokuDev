# MASTER PLAN DE INVESTIGACIÓN Y ARQUITECTURA: EL VERDADERO MVP DE KESSOKU DEV (OCTUBRE 2026)

**Proyecto:** Kessoku Dev (Micro-Software Factory & Productized Tech Service)  
**Equipo Fundador:**  
* **Líder Técnico & Arquitectura:** Licenciatura en Tecnologías de la Información (LTIN - CUCEA)  
* **Líder Comercial & Crecimiento:** Licenciatura en Negocios Internacionales (LINI - CUCEA)  
**Campus Sede:** Centro Universitario de Ciencias Económico-Administrativas (CUCEA), Universidad de Guadalajara, Zapopan, Jalisco  
**Fecha de Elaboración:** Octubre de 2026  
**Estatus:** Hoja de Ruta Táctica y Operativa Oficial  

---

## RESUMEN EJECUTIVO: LA VERDAD DEL MVP EN 2026

Una landing page institucional (como la alojada en [angelkero.github.io/KessokuDev](https://angelkero.github.io/KessokuDev/)) es una tarjeta de presentación indispensable, pero **NO es el Producto Mínimo Viable (MVP) de una empresa de software productizado**. La landing solo mide atracción pasiva.

En el estado del arte de octubre de 2026, el verdadero MVP de Kessoku Dev valida de manera simultánea dos engranes operativos:

1. **La Viabilidad de Entrega (Delivery Machine):** Demostrar que un estudiante de LTIN puede ensamblar, personalizar y desplegar un sitio web a 60fps con Core Web Vitals de 100 en **menos de 4.5 horas netas de trabajo**, utilizando un motor modular de componentes LEGO y pipelines de extracción de datos con IA.
2. **La Viabilidad Comercial y Cobro (Paid Validation):** Demostrar que el cofundador de LINI puede cerrar a dueños de negocios locales de la Zona Metropolitana de Guadalajara en una sesión de 30 segundos usando una **maqueta viva hiperrealista** y cobrar un **50% de anticipo bancario ($3,750 a $6,250 MXN)** mediante una Hoja de Encargo de una sola página.

---

```
                            EL CUADRANTE DEL MVP 2026
                                        │
           ┌────────────────────────────┴────────────────────────────┐
           ▼                                                         ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────────────┐
│     1. EL GENERADOR DE MONOREPO       │ │       2. EL SHOWROOM INTERACTIVO      │
│        (THE ASSEMBLY ENGINE)          │ │         (THE LIVE SALES SANDBOX)      │
│                                       │ │                                       │
│ • Monorepo Astro 5 + Tailwind v4      │ │ • Maqueta ultra-realista desplegada   │
│ • 10 Componentes LEGO universales     │ │   en demo.kessokudev.com              │
│ • Server Islands para catálogo vivo   │ │ • Selector "God Mode" multigiro       │
│ • SLA de ensamblado: < 4.5 horas      │ │ • Cierre "Live Vibrate" en 30 seg.    │
└───────────────────────────────────────┘ └───────────────────────────────────────┘
           │                                                         │
           └────────────────────────────┬────────────────────────────┘
                                        │
           ┌────────────────────────────┴────────────────────────────┐
           ▼                                                         ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────────────┐
│     3. EL PIPELINE DE EXTRACCIÓN      │ │       4. LA VALIDACIÓN PAGADA         │
│        (ZERO-EFFORT INTAKE AGENT)     │ │        (PAID VALIDATION CADENCE)      │
│                                       │ │                                       │
│ • Google Places API (datos + fotos)   │ │ • Hoja de Encargo de 1 sola página    │
│ • Gemini Flash Vision OCR (catálogos) │ │ • 3 contratos con 50% de anticipo     │
│ • Transcripción de audios de WhatsApp │ │ • Retención ética de MRR por reporte  │
│ • SLA de extracción: < 24 horas       │ │ • Protocolo ético Hospital PyME       │
└───────────────────────────────────────┘ └───────────────────────────────────────┘
```

---

## 1. ARQUITECTURA TÉCNICA Y MOTOR MODULAR (STACK OCTUBRE 2026)

### A. Monorepo Schema-Driven (Turborepo / Workspaces)
Para evitar el caos de clonar repositorios independientes y mantener librerías desactualizadas, Kessoku Dev estandariza una estructura de monorepo:

```
kessoku-monorepo/
├── packages/
│   ├── kessoku-core-ui/           # Los 10 Bloques LEGO en Astro 5 + Tailwind v4
│   │   ├── Header.astro
│   │   ├── HeroAIDA.astro
│   │   ├── CatalogGrid.astro
│   │   ├── QuoterDrawer.astro     # Drawer interactivo con cálculo de IVA
│   │   ├── LivePriceBadge.astro   # Astro 5 Server Island (server:defer)
│   │   ├── TrustBadges.astro
│   │   ├── MapsBooking.astro
│   │   └── UniversalFooter.astro
│   └── kessoku-config-schema/     # Validación de contratos de datos con Zod
│       └── client.schema.ts
├── apps/
│   ├── showroom/                  # Maqueta comercial viva
│   └── client-instances/          # Instancias por cliente (despliegue en Cloudflare)
│       └── refaccionaria-zapopan/
└── tools/
    └── cli/scaffold-client.ts     # Script de inicialización de cliente en 60s
```

### B. Astro 5: Content Layer y Server Islands sin la Falacia del Rebuild
* **El error clásico:** Recompilar el sitio estático completo cada vez que el dueño del negocio edita una celda en su Google Sheet satura los límites de compilación y crea cuellos de botella.
* **El estándar 2026:**
  1. **Astro 5 Content Layer (`src/content.config.ts`):** Compila la estructura estática del catálogo en build time con tipado estricto (Zod) a 60fps desde el Edge de Cloudflare Pages.
  2. **Server Islands (`server:defer`):** Los bloques de precio y disponibilidad consultan en tiempo real la hoja de Google Sheets en el servidor. El cliente cambia un precio en su celular y se refleja de inmediato sin reconstruir el sitio.

```astro
<!-- ProductCard.astro con Server Island -->
<div class="product-card border border-[#1e293b] p-4 rounded-lg bg-[#0e1726]">
  <img src={product.imageUrl} alt={product.title} class="w-full h-40 object-cover rounded" />
  <h4 class="text-white font-bold mt-2">{product.title}</h4>
  <p class="text-xs text-[#94a3b8]">Código: {product.partNumber}</p>
  
  <!-- Server Island diferido: consulta micro-endpoint en edge o caché SWR -->
  <LivePriceBadge server:defer productId={product.id} fallbackPrice={product.price}>
    <span slot="fallback" class="text-sm text-[#94a3b8] font-mono">${product.price} MXN</span>
  </LivePriceBadge>
  
  <button data-add-quote={product.id} class="mt-3 w-full bg-[#1d4ed8] text-white text-xs py-2 rounded font-bold">
    + AGREGAR A COTIZACIÓN
  </button>
</div>
```

### C. Estrategia Segura de WhatsApp (Cero Riesgo de Baneo)
* **Nivel 1 (Estándar Inquebrantable del MVP):** Deep-links `wa.me` generados 100% en el cliente.
  - El navegador calcula subtotal, IVA del 16% y total.
  - Genera el enlace directo al WhatsApp del negocio:
    > *"Hola Refacciones del Bajío, solicito cotización formal de: 2x Baleros ($960), 1x Bomba de agua ($1,650). Total con IVA: $3,027.60 MXN. Cliente: Don Fernando."*
  - **Ventaja:** Cero servidores que mantener, costo $0 y **cero riesgo de baneo de la línea telefónica**.
* **Nivel 2 (Add-on de Automatización):** Conexión oficial a Meta Cloud API (1,000 conversaciones gratuitas al mes) para generar PDF con folio mediante webhooks autorizados.

### D. El "Sprint Técnico de 4.5 Horas" para el Desarrollador (LTIN)

| Minutos | Actividad Concreta |
| :---: | :--- |
| **00 - 30 min** | Correr script de andamiaje `scaffold-client.ts`, inyectar tokens de color en Tailwind v4 (`@theme`). |
| **30 - 75 min** | Cargar datos del catálogo extraídos por IA en Google Sheets / Content Layer, optimizar imágenes a WebP vía Sharp. |
| **75 - 135 min** | Ensamblar los componentes modulares y configurar el WhatsApp Quoter con el número verificado del cliente. |
| **135 - 180 min** | Configurar formulario de contacto con Resend API y sincronización a Google Sheets (Add-on 01). |
| **180 - 225 min** | Configurar DNS en Cloudflare, emitir SSL y vincular perfil de Google Maps. |
| **225 - 270 min** | Auditoría final de Google Lighthouse (meta >95 móvil) y exportar reporte técnico de entrega. |

---

## 2. EL SHOWROOM MVP: LA MAQUETA VIVA DE VENTA EN CAMPUS

### A. El Caso de Estudio Hiperrealista: "Refacciones & Autopartes del Bajío"
Para que la maqueta resuene con los dueños de negocios tradicionales que acuden a CUCEA:
* **Ubicación Ficticia pero Exacta:** Anillo Periférico Norte Manuel Gómez Morín #1420, Zapopan, Jal. (a 3 minutos de CUCEA).
* **Catálogo Real:** 24 piezas mecánicas críticas (bombas de agua, baleros dobles, kits de distribución, frenos cerámicos) con códigos de fabricante y precios reales ($480, $1,650, $3,200 MXN).
* **Acreditación:** Sello de "Distribuidor Mayorista Autorizado en Zapopan".

### B. El Protocolo de Cierre en 30 Segundos ("The Live Vibrate Pitch")
1. **Segundos 0 a 08 (Velocidad):** Abre la maqueta en su teléfono o tablet: *"Mire Don Fernando, carga en 0.4 segundos. En datos móviles lentos, si tarda más de 3 segundos, el 60% de los clientes se van a la competencia"*.
2. **Segundos 09 a 18 (El cotizador):** Busca "bomba", da clic en `+ Agregar a Cotización` y se abre el drawer con el desglose de IVA y total.
3. **Segundos 19 a 30 (El choque sensorial):** Le pregunta: *"¿Cuál es su número de WhatsApp?"*. Escribe su número en la casilla de prueba y da clic en *Enviar*. **En 3 segundos el teléfono en el bolsillo de Don Fernando vibra.** Saca su propio celular y ve la cotización lista.  
   **Cierre:** *"Esto es exactamente lo que recibirán sus vendedores. Sin hojas de papel perdidas y listo en 5 días hábiles"*.

### C. La Barra Flotante "God Mode" (`?godmode=true`)
Un conmutador en la esquina inferior de la maqueta que permite cambiar de giro comercial en vivo frente al cliente:
1. **Giro Comercial / Refaccionaria:** Activa catálogo de piezas físicas y cotizador a WhatsApp.
2. **Giro Taller / Servicios Profesionales:** Cambia a agenda de citas vinculada a Google Calendar (Add-on 02).
3. **Giro Exportador B2B (Visión LINI):** Cambia a inglés, precios en USD y genera Factura Proforma comercial para clientes en EE. UU./Canadá (Paquete 03).

---

## 3. INTAKE DE CONTENIDO CON IA: CERO FRICCIÓN ("CLIENT GHOSTING KILLER")

El 90% de los proyectos web se retrasan semanas porque el cliente no manda logos, fotos ni textos. Kessoku Dev resuelve esto mediante un pipeline en 4 pasos:

1. **Pre-flight Scraping con Google Places API (New):** Con solo pedirle el nombre del negocio en Google Maps, la API extrae en 15 segundos: dirección oficial, teléfono, horarios, coordenadas para el mapa, las 3 mejores reseñas y 10 fotos del local subidas por clientes.
2. **Reconstrucción Vectorial de Marca:** Si el cliente solo tiene una foto de su lona o uniforme, un pipeline de vectorización con IA lo convierte en un archivo SVG nítido con fondo transparente en 2 minutos.
3. **Extracción de Catálogo con Gemini Flash Vision:** Don Fernando toma 3 fotos con su celular a su lista de precios arrugada o envía el PDF de su proveedor mayorista. Gemini Flash Vision procesa el documento y genera el JSON estructurado con SKU, título, categoría y precio en segundos.
4. **Notas de Voz por WhatsApp (Principio Draft-First):** Se le piden 2 audios informales por WhatsApp: *"Dígame sus 3 servicios estrella y qué garantía ofrece"*. Se transcriben y en **24 horas se le presenta al cliente el sitio casi terminado**. El cliente nunca ve un lienzo en blanco; solo valida y corrige.

---

## 4. VALIDACIÓN REAL, CONTRATOS Y UNIT ECONOMICS

### A. La Hoja de Encargo de 1 Página (Contrato B2B Ágil)

```
+----------------------------------------------------------------------------------------------------+
| KESSOKU DEV // DESPACHO DE INGENIERÍA DIGITAL & SOFTWARE PRODUCTIZADO                              |
| Sede: Torre CUCEA Smart Campus, Piso 2, Zapopan, Jal. | Contacto: contacto@kessokudev.com          |
+----------------------------------------------------------------------------------------------------+
| ORDEN DE SERVICIO TÉCNICO Y HOJA DE ENCARGO B2B                               FOLIO: #KD-2026-001   |
| Fecha: ____ de ___________ de 2026                                                                 |
+----------------------------------------------------------------------------------------------------+
| 1. DATOS FISCALES / COMERCIALES DEL CLIENTE:                                                       |
| Empresa: _____________________________________________ Titular: ___________________________________ |
| Giro Comercial: ______________________________________ WhatsApp / Celular: ________________________ |
+----------------------------------------------------------------------------------------------------+
| 2. PAQUETE SELECCIONADO Y ALCANCE CERRADO:                                                         |
| [ ] Paquete 01: Presencia Digital & Google Maps ($7,500 MXN setup + $1,499 MXN/mes)                 |
| [X] Paquete 02: Catálogo Interactivo & Cotizador WhatsApp ($12,500 MXN setup + $1,999 MXN/mes)     |
| [ ] Paquete 03: Plataforma Comercial & Expansión LINI ($18,500 MXN setup + $2,799 MXN/mes)         |
|                                                                                                    |
| ADD-ONS SELECCIONADOS:                                                                             |
| [ ] Add-on 01: Sincronización Google Sheets en tiempo real (+$1,800 MXN)                           |
| [ ] Add-on 02: Agenda Citas Google Calendar automatizada (+$2,200 MXN)                             |
| [ ] Add-on 03: Botón de Cobro con Tarjeta / SPEI / Mercado Pago (+$3,500 MXN)                      |
|                                                                                                    |
| COMPROMISO TÉCNICO: Carga <1 seg (Lighthouse >95), responsive móvil, certificado SSL, dominio     |
| propio por 1 año y vinculación a Google Maps.                                                      |
| REGLA DE ORO OPERATIVA: Cero desarrollos a la medida fuera de catálogo durante este encargo.       |
+----------------------------------------------------------------------------------------------------+
| 3. CALENDARIO DE ENTREGA GARANTIZADA:                                                              |
| Fecha de Inicio (Recepción del Anticipo): ____/____/2026                                            |
| Fecha de Puesta en Marcha en Producción: ____/____/2026 (5 a 7 días hábiles garantizados)          |
+----------------------------------------------------------------------------------------------------+
| 4. CONDICIONES ECONÓMICAS Y FORMA DE PAGO:                                                         |
| Inversión Total Setup: $12,500.00 MXN                                                              |
| • Anticipo Requerido (50% para inicio de ingeniería): $6,250.00 MXN                                |
| • Finiquito a la Entrega (50% contra acta de conformidad): $6,250.00 MXN                           |
| • Soporte Cloud, Mantenimiento & Analítica: $1,999.00 MXN / mes (a partir del Mes 2)               |
| CLABE Interbancaria (BBVA / STP): 012 320 0000000000 00 | Beneficiario: Kessoku Dev                |
+----------------------------------------------------------------------------------------------------+
| 5. CONFORMIDAD Y FIRMAS:                                                                           |
|                                                                                                    |
| __________________________________________        __________________________________________       |
| Por el Cliente / Titular del Negocio              Por Kessoku Dev (Fundadores CUCEA UdeG)          |
+----------------------------------------------------------------------------------------------------+
```

### B. Unit Economics del Modelo Universitario

```
+-----------------------------------------+--------------------+--------------------+--------------------+
| CONCEPTO FINANCIERO                     | PAQUETE 01 ($7.5k) | PAQUETE 02 ($12.5k)| PAQUETE 03 ($18.5k)|
+-----------------------------------------+--------------------+--------------------+--------------------+
| Setup Bruto Facturado                   | $7,500 MXN         | $12,500 MXN        | $18,500 MXN        |
| Costo Dominio .com (Año 1)              | ~$350 MXN          | ~$350 MXN          | ~$350 MXN          |
| Hosting Cloudflare Pages & SSL          | $0 MXN             | $0 MXN             | $0 MXN             |
| Costos Tokens IA (Gemini Flash OCR)     | ~$5 MXN            | ~$15 MXN           | ~$30 MXN           |
| Costo Directo Total                     | ~$355 MXN          | ~$365 MXN          | ~$380 MXN          |
+-----------------------------------------+--------------------+--------------------+--------------------+
| Margen Bruto Directo                    | 95.2% ($7,145 MXN) | 97.0% ($12,135 MXN)| 97.9% ($18,120 MXN)|
| Horas Netas Totales (LTIN + LINI)       | 5.0 horas          | 7.5 horas          | 11.0 horas         |
| Rendimiento por Hora del Equipo         | $1,429 MXN / hora  | $1,618 MXN / hora  | $1,647 MXN / hora  |
+-----------------------------------------+--------------------+--------------------+--------------------+
```

### C. Retención Ética de MRR: Reporte de ROI en WhatsApp
Para evitar cancelaciones de la cuota mensual de $1,499 o $1,999 MXN:
* **El día 1 de cada mes a las 9:00 AM**, el cliente recibe en WhatsApp:
  > *"Don Fernando, resumen mensual de Refacciones del Bajío: En octubre su sitio web tuvo 640 visitas, 82 personas abrieron el catálogo de piezas y se generaron 27 cotizaciones directas a su WhatsApp por un valor estimado de $54,000 MXN. Su plataforma operó con 100% de disponibilidad"*.
* Al comprobar el retorno directo de inversión, pagar la cuota de soporte se vuelve indispensable.

---

## 5. HOJA DE RUTA TÁCTICA A 14 DÍAS PARA LOS FUNDADORES

```
DÍAS 01 - 03: CONSTRUCCIÓN DEL GENERADOR Y SHOWROOM (TECH LEAD - LTIN)
├── Configurar el monorepo en Astro 5 y definir tokens en Tailwind v4 (@theme).
├── Implementar los 10 bloques LEGO universales en packages/kessoku-core-ui/.
├── Configurar Server Islands (server:defer) para precios dinámicos de Google Sheets.
└── Desplegar 'demo.kessokudev.com' (Refacciones del Bajío) con selector "God Mode".

DÍAS 04 - 06: PIPELINE MULTIMODAL Y MATERIAL COMERCIAL (COMMERCIAL LEAD - LINI)
├── Configurar script de extracción de Google Places API (New) y vectorizador de logos.
├── Conectar el extractor de catálogo Gemini Flash Vision para fotos de listas de precios.
├── Imprimir 20 ejemplares del One-Pager formal (Cara 1 PyME / Cara 2 CUCEA).
└── Preparar carpetas con 10 Hojas de Encargo de 1 Página numeradas.

DÍAS 07 - 10: PROSPECCIÓN EN CAMPUS Y AUDITORÍAS DE 30 MINUTOS (DUPLA LINI + LTIN)
├── Entrevistarse con el Mtro. Rogelio Rico (P-102) para registrarse como aliados técnicos.
├── Prospección presencial con 8 a 10 empresas que acuden a asesorías a Hospital PyME.
└── Ejecutar la técnica "Live Vibrate" en el iPad/celular haciendo vibrar el WhatsApp del dueño.

DÍAS 11 - 14: CIERRE, ENTREGA RÁPIDA Y PRIMER COBRO DE FINIQUITO (AMBOS)
├── Cerrar los primeros 3 contratos con 50% de anticipo bancario ($3,750 a $6,250 MXN c/u).
├── Extraer el catálogo y fotos en menos de 24 horas usando el pipeline de IA.
├── Ensamblar y desplegar los sitios en menos de 5 días hábiles (<4.5 horas netas por sitio).
└── Cobro del 50% de finiquito contra acta de conformidad y activación del MRR mensual.
```

---
*Fin del Master Plan Operativo — Kessoku Dev Octubre 2026.*
