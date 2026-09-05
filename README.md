#  Practica-AG: Optimización Combinatoria con Algoritmos Genéticos

##  Introducción
Este proyecto implementa soluciones basadas en **Algoritmos Genéticos** para resolver problemas de optimización combinatoria con restricciones, inspirados en el **Problema de la Mochila**. El objetivo es maximizar funciones de aptitud (fitness) bajo limitaciones específicas como presupuestos, números fijos de elementos y reglas de selección.

---

##  Herramientas y Tecnologías Utilizadas

| Herramienta | Versión/Descripción | Uso en el Proyecto |
| :--- | :--- | :--- |
| **Python** | 3.14.4 | Lenguaje de programación principal. |
| **Visual Studio Code** | Editor de código | Desarrollo, edición de notebooks y gestión de Git. |
| **Jupyter Notebook** | Extensión de VS Code | Entorno interactivo para desarrollo y visualización. |
| **Git & GitHub** | Control de versiones | Gestión de ramas, commits y colaboración en equipo. |
| **Entorno Virtual** | `venv` | Aislamiento de dependencias del proyecto. |

###  Librerías Principales
- **NumPy**: Cálculos numéricos y manipulación de arrays (cromosomas).
- **Pandas**: Estructura y análisis de datos de proyectos/candidatos.
- **Matplotlib**: Visualización de gráficos (evolución del fitness, distribución de recursos).

> **Instalación de dependencias:**
> ```bash
> pip install numpy pandas matplotlib
> ```

---

## Estructura del Proyecto

```text
Practica-AG/
├── README.md                  # Documentación principal (este archivo)
├── .gitignore                 # Archivos excluidos del repositorio (venv, temp, etc.)
├── Ejercicios_practicos/      # Carpeta con los notebooks de los ejercicios
│   ├── Ejercicio1_inversiones.ipynb  # Portafolio de inversiones
│   ├── Ejercicio2_seleccion_personal.ipynb # Selección de personal
│   └── Ejercicio3_cruzamiento.ipynb   # Operador de cruzamiento de dos puntos
└── venv/                      # Entorno virtual (excluido por .gitignore)


## Integrantes 

Integrante	               Rama	                               Ejercicios Resueltos
Yecid Villamil	feature/Yecid_Villamil_AG	Ejercicio 1 (Portafolio) y Ejercicio 4 (Análisis)
Yesid Martinez	feature/Yesid_Martinez_AG	Ejercicio 2 (Selección de Personal) y Ejercicio 3 (Cruzamiento)