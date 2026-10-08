# ⚡ Kessoku Dev

> Startup de desarrollo de software, inteligencia de negocios y automatización operativa impulsada por IA.

---

## 👥 Equipo Fundador
* **Líder Técnico / Arquitecto de Software & IA:** Licenciatura en Tecnologías de la Información (LTIN - CUCEA) & Full Stack.
* **Líder Comercial / Crecimiento & Alianzas:** Licenciatura en Negocios Internacionales (LINI - CUCEA).

---

## 🛠️ Stack & Herramientas de Desarrollo

### 1. Spec-Driven Development (SDD): OpenSpec
* **CLI:** `openspec` (v1.14.1) instalado global y localmente.
* **Directorio de Especificaciones:** [`openspec/`](file:///Users/angelzaragoza/Desktop/KessokuDev/openspec/)
* **Flujos soportados:** Antigravity, Gemini CLI, Cursor, Claude Code.
* **Comandos rápidos:**
  * Proponer un cambio: `openspec change <nombre>` o `/opsx-propose`
  * Validar especificaciones: `openspec validate`
  * Ver dashboard interactivo: `openspec view`

### 2. Knowledge Graph & Codebase Intelligence: Graphify
* **CLI & Motor:** `graphify` (v0.9.80) instalado en entorno Python.
* **Directorio de Grafo:** [`graphify-out/`](file:///Users/angelzaragoza/Desktop/KessokuDev/graphify-out/)
* **Comandos rápidos:**
  * Indexar cambios: `graphify . --code-only`
  * Consultar relaciones: `graphify query "<pregunta>"`
  * Ver reporte de arquitectura: `cat graphify-out/graph.json`

### 3. Design System & Frontend Excellence: Impeccable
* **Repositorio & Motor:** [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
* **Instalación:** Habilitado localmente en `.agent/`, `.claude/`, `.cursor/`, `.gemini/` con binarios nativos del motor `impeccable`.
* **Uso:** Todas las decisiones de UI/UX, componentes y animaciones se rigen bajo los principios de *Impeccable* (craft, jerarquía visual, a11y, responsive, tipografía y movimiento con propósito).
* **Comandos rápidos:**
  * Iniciar contexto de diseño: `/impeccable init`
  * Auditoría técnica de diseño: `/impeccable audit`
  * Pulido de interfaces: `/impeccable polish`
  * Escanear anti-patrones de UI: `.agent/skills/impeccable/scripts/impeccable detect`

---

## 📂 Estructura del Repositorio

```text
KessokuDev/
├── docs/
│   ├── comercial/
│   │   ├── ONE_PAGER_KESSOKU_DEV.md    # One-Pager comercial e institucional (doble cara)
│   │   ├── ONE_PAGER_KESSOKU_DEV.pdf   # Versión lista para imprimir en A4
│   │   └── ONE_PAGER_KESSOKU_DEV.html  # Plantilla web maquetada
│   └── ecosistema-cucea/
│       ├── REPORTE_ECOSISTEMA_CUCEA_KESSOKU_DEV.md  # Investigación exhaustiva territorial
│       ├── REPORTE_ECOSISTEMA_CUCEA_KESSOKU_DEV.pdf # Dossier ejecutivo maquetado
│       └── REPORTE_ECOSISTEMA_CUCEA_KESSOKU_DEV.html # Versión HTML
├── openspec/                          # Especificaciones de arquitectura SDD
│   ├── config.yaml
│   ├── changes/
│   └── specs/
├── graphify-out/                      # Grafo de conocimiento e indexación
│   └── graph.json
├── scripts/
│   ├── generate_pdf.py                # Compilador de reportes a PDF vía Chrome Headless
│   └── compile_one_pager.py           # Compilador de One-Pager a PDF
└── README.md
```

---

## 🚀 Próximos Pasos Operativos
1. **Validación Institucional en Campus:**
   * Llevar el [`ONE_PAGER_KESSOKU_DEV.pdf`](file:///Users/angelzaragoza/Desktop/KessokuDev/docs/comercial/ONE_PAGER_KESSOKU_DEV.pdf) (Cara 2) a la Mtra. Daniela Gómez en el Edificio CIADEyS (CEIS) para registro en CUCEA Emprende.
   * Tramitar acceso al Coworking del Piso 2 de la Torre CUCEA Smart Campus.
   * Acordar reunión con el Mtro. Rogelio Rico Huerta (Hospital PyME) en Módulo P.
2. **Construcción de Activos Digitales:**
   * Inicializar la Landing Page insignia de Kessoku Dev aplicando el estándar *Impeccable*.
   * Preparar la demo interactiva del Bot Cotizador y Tablero de BI.
