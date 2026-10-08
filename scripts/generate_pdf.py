import subprocess
import os

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Reporte Integral - Ecosistema CUCEA y Oportunidades Tecnológicas</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

  @page {
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-right {
      content: counter(page);
    }
  }

  body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #1e293b;
    line-height: 1.6;
    font-size: 13px;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
  }

  /* Header Cover / Hero */
  .cover {
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 24px;
    margin-bottom: 30px;
  }

  .badge {
    display: inline-block;
    padding: 4px 12px;
    background: #e0e7ff;
    color: #3730a3;
    font-weight: 700;
    font-size: 10px;
    border-radius: 9999px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 12px;
  }

  h1 {
    font-size: 24px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.25;
    margin: 0 0 12px 0;
    letter-spacing: -0.02em;
  }

  .subtitle {
    font-size: 13px;
    color: #64748b;
    margin-bottom: 16px;
    font-weight: 500;
  }

  .meta-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 11.5px;
  }

  .meta-item strong {
    color: #0f172a;
    display: block;
    font-size: 10.5px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    color: #475569;
  }

  h2 {
    font-size: 16px;
    font-weight: 700;
    color: #0f172a;
    border-left: 4px solid #3b82f6;
    padding-left: 10px;
    margin-top: 32px;
    margin-bottom: 14px;
    letter-spacing: -0.01em;
    page-break-after: avoid;
  }

  h3 {
    font-size: 13.5px;
    font-weight: 700;
    color: #1e293b;
    margin-top: 20px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }

  p {
    margin: 0 0 12px 0;
    color: #334155;
  }

  ul, ol {
    margin: 0 0 14px 0;
    padding-left: 20px;
    color: #334155;
  }

  li {
    margin-bottom: 6px;
  }

  /* Callout box */
  .callout {
    background: #eff6ff;
    border-left: 4px solid #2563eb;
    border-radius: 0 8px 8px 0;
    padding: 14px 16px;
    margin: 18px 0;
    page-break-inside: avoid;
  }

  .callout-title {
    font-weight: 700;
    color: #1d4ed8;
    font-size: 12.5px;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .callout-warning {
    background: #fef2f2;
    border-left: 4px solid #ef4444;
  }

  .callout-warning .callout-title {
    color: #b91c1c;
  }

  /* Diagrams / Code blocks */
  pre {
    background: #0f172a;
    color: #f1f5f9;
    padding: 14px 16px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
    line-height: 1.45;
    overflow-x: auto;
    page-break-inside: avoid;
    margin: 16px 0;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 11.5px;
    page-break-inside: avoid;
  }

  th {
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    text-align: left;
    padding: 8px 12px;
    border-bottom: 2px solid #cbd5e1;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }

  td {
    padding: 8px 12px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
    vertical-align: top;
  }

  tr:nth-child(even) td {
    background: #fafafa;
  }

  /* Value Ladder Graphic */
  .ladder-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 20px 0;
    page-break-inside: avoid;
  }

  .ladder-step {
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px 16px;
    background: #ffffff;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .ladder-step.s1 { border-left: 5px solid #10b981; background: #f0fdf4; }
  .ladder-step.s2 { border-left: 5px solid #0ea5e9; background: #f0f9ff; }
  .ladder-step.s3 { border-left: 5px solid #6366f1; background: #eef2ff; }
  .ladder-step.s4 { border-left: 5px solid #8b5cf6; background: #f5f3ff; }

  .ladder-info h4 {
    margin: 0 0 4px 0;
    font-size: 13px;
    font-weight: 700;
    color: #0f172a;
  }

  .ladder-info p {
    margin: 0;
    font-size: 11px;
    color: #64748b;
  }

  .ladder-price {
    font-weight: 800;
    font-size: 14px;
    color: #0f172a;
    white-space: nowrap;
    margin-left: 16px;
  }

  .page-break {
    page-break-before: always;
  }

  .footer-note {
    font-size: 10px;
    color: #94a3b8;
    text-align: center;
    margin-top: 30px;
    border-top: 1px solid #e2e8f0;
    padding-top: 12px;
  }
</style>
</head>
<body>

<div class="cover">
  <div class="badge">Estrategia de Mercado & Inteligencia Territorial</div>
  <h1>Radiografía Integral del Ecosistema CUCEA: Infraestructura, Programas y Oportunidades Tecnológicas para PyMEs</h1>
  <div class="subtitle">Documento Oficial de Inteligencia Operativa para la Entrada al Mercado de Kessoku Dev</div>
  
  <div class="meta-grid">
    <div class="meta-item">
      <strong>Proyecto</strong>
      Kessoku Dev (Agencia & Estudio de Tecnología)
    </div>
    <div class="meta-item">
      <strong>Campus Sede</strong>
      CUCEA - Universidad de Guadalajara (Zapopan, Jal.)
    </div>
    <div class="meta-item">
      <strong>Dupla Fundadora</strong>
      Líder Técnico (Ingeniería en Negocios / BI & Full Stack)<br>
      Líder Comercial (Lic. en Negocios Internacionales - LINI)
    </div>
    <div class="meta-item">
      <strong>Fecha & Ciclo</strong>
      Octubre 2026 | Fase de Validación y Tracción Inicial
    </div>
  </div>
</div>

<h2>1. Resumen Ejecutivo y Tesis de Negocio</h2>
<p>
  El presente informe sintetiza la investigación territorial e institucional sobre el <strong>Centro Universitario de Ciencias Económico Administrativas (CUCEA)</strong> con el fin de guiar las operaciones de <strong>Kessoku Dev</strong>. La premisa central del proyecto es transformar la capacidad de producción ágil de software e inteligencia de negocios en una oferta de alto valor para las pequeñas y medianas empresas (PyMEs) de la Zona Metropolitana de Guadalajara (ZMG).
</p>

<div class="callout">
  <div class="callout-title">💡 La Falla de Mercado Detectada: "The Implementation Void" (El Vacío de Implementación)</div>
  <p>
    En CUCEA confluyen anualmente cientos de dueños de micro y pequeñas empresas buscando auxilio empresarial a través del <strong>Hospital PyME</strong> y de <strong>IDITpyme</strong>. Tras recibir hasta 5 sesiones de consultoría gratuita, el cuerpo académico les entrega un diagnóstico exhaustivo en PDF que dictamina que la empresa está perdiendo dinero por descontrol de inventarios, cotizaciones manuales lentas en WhatsApp y una dependencia crítica de hojas de cálculo desconectadas.
  </p>
  <p style="margin: 0; font-weight: 600;">
    Aquí se produce el abandono: CUCEA no cuenta con programadores ni presupuesto para desarrollarles software, y las casas de desarrollo privadas de Guadalajara les cobran presupuestos de $80,000 a $250,000 MXN. Las empresas quedan en un limbo operativo. Kessoku Dev entra exactamente en este punto de dolor con soluciones paquetizadas y entregables inmediatos.
  </p>
</div>

<h2>2. Infraestructura Física: Los Edificios del Emprendimiento en Campus</h2>
<p>
  Para responder con total precisión a la geografía del campus, en CUCEA existen dos complejos verticales y una unidad administrativa que articulan los programas de negocios:
</p>

<pre>
+---------------------------------------------------------------------------------------------------------------+
|                                      CAMPUS CUCEA (NÚCLEO LOS BELENES)                                         |
+---------------------------------------------------------------------------------------------------------------+
|  1. EDIFICIO CIADEyS / CIADES              2. LA TORRE CUCEA SMART               3. EDIFICIO DE VINCULACIÓN   |
|     (Zona de Posgrados)                       (Zona Central del Campus)             (Módulo P - Planta Baja)  |
|     * Sede del CEIS (Centro de Emprendimiento   * Edificio vertical de 8 niveles      * Sede física de IDITpyme |
|       e Innovación Social)                    * Piso 2: Coworking & Smart Learning    (Oficina P-102)         |
|     * Sede de la Incubadora CUCEA Emprende    * Piso 3: B-Learning & CUCEA Plus     * Ventanilla de atención  |
|     * Pre-incubación, validación de modelos   * Piso 5: Medios Creativos/Multimedia   de Hospital PyME        |
|       y retos de innovación                   * Piso 6: Transferencia Tecnológica   * Módulo O (Planta Alta): |
|     * Absorbió al CIEE y LINE                 * Espacio operativo para startups       Prácticas y Convenios   |
+---------------------------------------------------------------------------------------------------------------+
|  * Aclaración de Desmitificación: CERi (Centro de Recursos Informativos)                                      |
|    Es la BIBLIOTECA CENTRAL del CUCEA. NO es una incubadora de empresas. Su mención constante entre alumnos  |
|    se debe a la similitud fonética con CEIS / CIEE y al uso de sus salas de cómputo para estudio.             |
+---------------------------------------------------------------------------------------------------------------+
</pre>

<h3>A. Edificio CIADEyS / CIADES (Centro de Innovación para el Aceleramiento al Desarrollo Económico y Social)</h3>
<ul>
  <li><strong>Ubicación:</strong> Zona de Posgrados (frente al Módulo P, cerca de la Biblioteca CERi).</li>
  <li><strong>Rol Histórico:</strong> Es el edificio tradicional de emprendimiento estudiantil. En él se fusionaron las funciones del extinto <strong>CIEE</strong> (Centro Internacional de Excelencia Empresarial) y del <strong>LINE</strong> (Laboratorio de Innovación y Emprendimiento).</li>
  <li><strong>CEIS (Centro de Emprendimiento e Innovación Social):</strong> Coordinado por la <strong>Mtra. Daniela Gómez Montemayor</strong>. Espacio oficial para canalizar proyectos universitarios, mentorías iniciales y registro formal de incubación.</li>
  <li><strong>Incubadora "CUCEA Emprende":</strong> Programa estructurado de aceleración y validación de modelos de negocio.</li>
</ul>

<h3>B. Torre CUCEA Smart Campus (Edificio Vertical de 8 Pisos)</h3>
<ul>
  <li><strong>Ubicación:</strong> Zona central del campus, anexa a la explanada cívica y servicios administrativos.</li>
  <li><strong>Piso 2 (Smart Learning & Coworking):</strong> Estaciones de trabajo colaborativo, conectividad de alta velocidad y salas para startups universitarias formalmente incubadas.</li>
  <li><strong>Piso 5 (Medios Creativos):</strong> Estudios y cabinas de producción multimedia para generación de demos y materiales de difusión.</li>
  <li><strong>Pisos 6 a 8:</strong> Oficinas de investigación aplicada, vinculación con el sector público y clústeres empresariales de Jalisco.</li>
</ul>

<h3>C. Edificio de Vinculación Empresarial (Módulo P)</h3>
<ul>
  <li><strong>IDITpyme (Módulo P-102):</strong> Instituto con más de 20 años de trayectoria enfocado en desarrollo de PyMEs, diagnósticos con sistemas expertos, capacitación y trámites de propiedad intelectual (marcas/patentes ante el IMPI).</li>
  <li><strong>Hospital PyME:</strong> Programa de consultoría y vinculación gratuita con más de 100 expertos y estudiantes de posgrado.</li>
</ul>

<div class="page-break"></div>

<h2>3. Directorio de Autoridades y Tomadores de Decisión</h2>
<table>
  <thead>
    <tr>
      <th>Instancia</th>
      <th>Responsable / Titular</th>
      <th>Ubicación Física</th>
      <th>Medios de Contacto</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Rectoría de CUCEA</strong></td>
      <td>Dra. Mara Nadiezhda Robles Villaseñor (2025-2028)</td>
      <td>Edificio de Rectoría</td>
      <td>Conmutador: 33 3770 3300</td>
    </tr>
    <tr>
      <td><strong>CEIS / CIADEyS / CUCEA Emprende</strong></td>
      <td>Mtra. Daniela Gómez Montemayor</td>
      <td>Edificio CIADEyS (Posgrados)</td>
      <td>Ext. 25916 / 25792<br><code>ceis@cucea.udg.mx</code><br><code>ciades@cucea.udg.mx</code></td>
    </tr>
    <tr>
      <td><strong>Hospital PyME</strong></td>
      <td>Mtro. Rogelio Rolando Rico Huerta</td>
      <td>Módulo P (Vinculación)</td>
      <td>Ext. 25505<br><code>dudas@cucea.udg.mx</code><br><code>hospitalpyme.cucea.udg.mx</code></td>
    </tr>
    <tr>
      <td><strong>IDITpyme</strong></td>
      <td>Dr. Ricardo Arechavala Vargas</td>
      <td>Módulo P-102 (Planta Baja)</td>
      <td>Ext. 25501 / 25504<br>WhatsApp: 33 2623 2909<br><code>iditpyme.admon@gmail.com</code></td>
    </tr>
    <tr>
      <td><strong>Prácticas y Convenios</strong></td>
      <td>Unidad de Vinculación</td>
      <td>Edificio O (Planta Alta)</td>
      <td>Atención institucional a empresas y alumnos</td>
    </tr>
  </tbody>
</table>

<h2>4. Radiografía de las PyMEs Locales y sus Dolores Endémicos</h2>
<p>
  Las PyMEs que se acercan a CUCEA pertenecen mayoritariamente a giros tradicionales de Zapopan y Guadalajara: manufactura ligera (calzado, muebles, empaques, textil), comercio mayorista/minorista (abarrotes, ferreterías, autopartes) y servicios o alimentos. Facturan entre <strong>$80,000 y $800,000 MXN mensuales</strong> y sufren de cuatro cuellos de botella estructurales:
</p>

<table>
  <thead>
    <tr>
      <th>Dolor Observable</th>
      <th>Causa Raíz Técnica</th>
      <th>Impacto Financiero Negativo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. El "Infierno de Excels"</strong></td>
      <td>15 a 30 hojas de cálculo desconectadas; fórmulas manipuladas a mano; sin respaldos automáticos en la nube.</td>
      <td>10 a 15 horas semanales perdidas en retrabajos; errores frecuentes en cotizaciones; descuadres graves de stock.</td>
    </tr>
    <tr>
      <td><strong>2. El "Embudo Ciego de WhatsApp"</strong></td>
      <td>Cotizaciones manuales desde teléfonos personales de los vendedores; nula trazabilidad comercial.</td>
      <td>Fuga del 30% al 45% de prospectos; si el vendedor se va, se lleva la cartera de clientes.</td>
    </tr>
    <tr>
      <td><strong>3. Ceguera de Rentabilidad</strong></td>
      <td>El dueño monitorea el saldo bancario pero desconoce el margen de contribución real por producto.</td>
      <td>Venta involuntaria de productos a pérdida; subsidio de clientes morosos sin advertirlo a tiempo.</td>
    </tr>
    <tr>
      <td><strong>4. Fricción Fiscal SAT y Cobranza</strong></td>
      <td>Emisión manual en el portal del SAT (CFDI 4.0); olvido de complementos de pago; cobranza desfasada.</td>
      <td>Riesgo de sanciones fiscales; cartera vencida que ahorca el flujo de caja semanal de la empresa.</td>
    </tr>
  </tbody>
</table>

<h2>5. Catálogo de Soluciones Tecnológicas de Kessoku Dev</h2>
<p>
  Aprovechando la dupla entre <strong>Ingeniería en Negocios / BI & Full Stack</strong> y <strong>Negocios Internacionales</strong>, la oferta se diversifica más allá del desarrollo web convencional:
</p>

<table>
  <thead>
    <tr>
      <th>Línea de Solución</th>
      <th>Arquitectura Técnica</th>
      <th>Entregable Concreto de Negocio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. BI & Data Pipelines Operativos</strong></td>
      <td>PostgreSQL / Supabase + Metabase o PowerBI Embedded. ETL en Node.js/Python.</td>
      <td>Tablero ejecutivo en tiempo real con 4 métricas vitales: margen de contribución, rotación de stock, Pareto de clientes y proyección de flujo de caja. Migración limpia desde Excel.</td>
    </tr>
    <tr>
      <td><strong>2. Embudo Comercial & Cotizador WhatsApp</strong></td>
      <td>WhatsApp Cloud API + n8n / Make + Airtable / CRM ligero.</td>
      <td>Bot conversacional que emite cotizaciones en PDF oficial con precios actualizados en &lt;60 segundos, registra prospectos y programa recordatorios de seguimiento.</td>
    </tr>
    <tr>
      <td><strong>3. Mini-ERP y Portal Web Operativo</strong></td>
      <td>Next.js / Tailwind CSS + Facturapi (CFDI 4.0) + Supabase. PWA móvil.</td>
      <td>Aplicación ligera para celular y computadora: lectura de códigos QR de almacén, notas de entrega con firma digital y timbrado automático de facturas ante el SAT.</td>
    </tr>
    <tr>
      <td><strong>4. Suite Digital de Exportación (B2B)</strong></td>
      <td>Portal B2B multimoneda + APIs de cálculo logístico + Generador de PDFs.</td>
      <td>Calculadora automática de cubicaje de tarimas, estimación de fletes, aplicación de Incoterms 2020 y generación inmediata de Factura Proforma y Packing List oficial.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h2>6. Estrategia Comercial: La Escalera de Valor (Ladder of Value)</h2>
<p>
  Para derribar la resistencia al cambio de las PyMEs locales, la estrategia comercial divide el proceso en cuatro niveles progresivos:
</p>

<div class="ladder-container">
  <div class="ladder-step s1">
    <div class="ladder-info">
      <h4>NIVEL 1: Gancho Gratuito — "Auditoría Digital de Procesos"</h4>
      <p>Sesión diagnóstica de 30 minutos (presencial en Torre Smart o virtual) donde se mapean las fugas de tiempo y dinero y se entregan 2 soluciones de impacto inmediato.</p>
    </div>
    <div class="ladder-price">Gratis ($0)</div>
  </div>

  <div class="ladder-step s2">
    <div class="ladder-info">
      <h4>NIVEL 2: Producto de Entrada (Quick-Win)</h4>
      <p>Bot cotizador de WhatsApp o Dashboard de Ventas en Metabase. Tiempo de entrega garantizado en 7 a 10 días naturales para evidenciar retorno de inversión veloz.</p>
    </div>
    <div class="ladder-price">$6,000 – $12,000 MXN</div>
  </div>

  <div class="ladder-step s3">
    <div class="ladder-info">
      <h4>NIVEL 3: Implementación Core Integral</h4>
      <p>Mini-ERP de almacén con códigos QR, Portal B2B o Suite de Exportación integrada con timbrado SAT CFDI 4.0. Esquema de pago por hitos (50% anticipo, 25% avance, 25% entrega).</p>
    </div>
    <div class="ladder-price">$18,000 – $35,000 MXN</div>
  </div>

  <div class="ladder-step s4">
    <div class="ladder-info">
      <h4>NIVEL 4: Retenedor Mensual Recurrente (MRR)</h4>
      <p>Mantenimiento de infraestructura cloud (Vercel/Supabase), soporte para WhatsApp, respaldos programados de bases de datos y 4 horas mensuales de mejoras evolutivas.</p>
    </div>
    <div class="ladder-price">$2,500 – $5,000 MXN / mes</div>
  </div>
</div>

<h2>7. Cumplimiento Normativo y Penetración en Campus</h2>

<div class="callout callout-warning">
  <div class="callout-title">⚠️ Blindaje Ético y Legal Obligatorio</div>
  <p style="margin: 0;">
    Queda terminantemente descartada cualquier extracción no autorizada de expedientes o bases de datos de servicio social o programas universitarios. Esto vulneraría el <em>Reglamento General de Prestación de Servicio Social de la UdeG</em> y la legislación de protección de datos personales en posesión de entidades públicas. Toda la estrategia debe ejecutarse a través de canales institucionales y transparentes.
  </p>
</div>

<h3>La Ruta Institucional Legítima</h3>
<ol>
  <li><strong>Incubación en CUCEA Emprende / CEIS:</strong> Registro formal del proyecto en la convocatoria vigente del CEIS (Edificio CIADEyS). Otorga legitimidad universitaria, uso del espacio de Coworking del Piso 2 en la Torre Smart y respaldo como startup incubada.</li>
  <li><strong>Alianza de Derivación con Hospital PyME e IDITpyme:</strong> Acercamiento formal con los coordinadores para posicionar a Kessoku Dev como el brazo de desarrollo técnico de alumnos avalados para empresas que terminan sus 5 sesiones gratuitas.</li>
  <li><strong>Talleres Gratuitos de Atracción de Leads:</strong> Impartición del taller bimestral <em>"De Excel a la Automatización: Guía Práctica para la PyME"</em> en las instalaciones de la Torre Smart, convocando a empresarios de Hecho en Zapopan y Hospital PyME. Al terminar, se ofrece la Auditoría Digital de 30 minutos sin costo.</li>
</ol>

<h2>8. Plan de Acción Inmediato (Roadmap a 30 Días)</h2>
<table>
  <thead>
    <tr>
      <th>Periodo</th>
      <th>Objetivo Principal</th>
      <th>Responsable</th>
      <th>Entregable Concreto</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Semana 1</strong></td>
      <td>Registro formal en CEIS (Edificio CIADEyS) y trámite de acceso a Coworking (Torre Smart, Piso 2).</td>
      <td>Ambos fundadores</td>
      <td>Solicitud de incubación presentada y acreditación de proyecto.</td>
    </tr>
    <tr>
      <td><strong>Semana 2</strong></td>
      <td>Elaboración del One-Pager comercial y montaje de demos funcionales (Bot WhatsApp + Dashboard BI muestra).</td>
      <td>Líder Técnico (Demos)<br>Líder Comercial (One-Pager)</td>
      <td>Documento comercial de 1 página y enlace navegable en Supabase/Metabase.</td>
    </tr>
    <tr>
      <td><strong>Semana 3</strong></td>
      <td>Cita formal con Mtro. Rogelio Rico (Hospital PyME) y Dr. Ricardo Arechavala (IDITpyme).</td>
      <td>Ambos fundadores</td>
      <td>Presentación de la propuesta como proveedores de solución recomendados.</td>
    </tr>
    <tr>
      <td><strong>Semana 4</strong></td>
      <td>Ejecución de las primeras 3 Auditorías Digitales Gratuitas y cierre de proyecto Quick-Win.</td>
      <td>Líder Comercial (Ventas)<br>Líder Técnico (Diagnóstico)</td>
      <td>Primer contrato de implementación firmado ($6,000 – $12,000 MXN).</td>
    </tr>
  </tbody>
</table>

<div class="footer-note">
  Kessoku Dev — Documento de Inteligencia Territorial e Investigación de Mercado. Elaborado para planeación estratégica y comercial.
</div>

</body>
</html>
"""

html_path = "/Users/angelzaragoza/Desktop/KessokuDev/REPORTE_ECOSISTEMA_CUCEA_KESSOKU_DEV.html"
pdf_path = "/Users/angelzaragoza/Desktop/KessokuDev/REPORTE_ECOSISTEMA_CUCEA_KESSOKU_DEV.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML escrito en {html_path}")

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    f"file://{html_path}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
    print(f"PDF generado exitosamente en {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
else:
    print(f"Error generando PDF: {res.stderr}")
