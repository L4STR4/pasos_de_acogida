# 🐾 Análisis de Estancia y Adopción en Refugio de Animales (Austin Animal Center)

## 📌 Descripción del Proyecto
Este proyecto de Análisis Exploratorio de Datos (EDA) examina el histórico de entradas y salidas del **Austin Animal Center** (con más de 150.000 registros) para identificar las variables clave que condicionan el tiempo de permanencia (`Days_in_Shelter`) de los animales en el refugio.

El objetivo principal es transformar estos hallazgos en soluciones de gestión interna y comunicación, optimizando las tasas de adopción y reduciendo la saturación de las instalaciones[cite: 1].

---

## 🎯 Objetivos e Hipótesis

### Objetivos
* **Identificar cuellos de botella:** Detectar qué perfiles de animales sufren estancias prolongadas.
* **Anticipar picos de demanda:** Analizar la estacionalidad de ingresos para coordinar recursos y casas de acogida.
* **Maximizar adopciones:** Proponer campañas hipersegmentadas basadas en patrones de datos reales[cite: 1].

### Hipótesis Planteadas
1. **El factor pelaje/raza:** Los animales de pelaje oscuro y tamaño grande permanecen una media de días significativamente mayor en la jaula antes de ser adoptados.
2. **Estacionalidad y saturación:** Los meses de primavera y verano concentran picos de recogidas en la calle (*Strays*), reduciendo la tasa de adopción rápida por sobreocupación.
3. **Condición al ingreso:** Los animales que ingresan heridos o enfermos presentan una menor probabilidad de adopción directa, requiriendo mayor tiempo de estancia o traslado.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Tratamiento de Datos:** `Pandas`, `NumPy`
* **Visualización:** `Matplotlib`, `Seaborn`
* **Entorno:** Jupyter Notebook / VS Code
* **Control de Versiones:** Git & GitHub

---

## 📁 Estructura del Repositorio

El código y los datos están organizados siguiendo la estructura estandarizada[cite: 1]:

```text
proyecto-eda-mascotas/
├── README.md                 # Presentación del proyecto y tecnologías utilizadas
└── src/
    ├── main.ipynb            # Notebook principal con el flujo completo de análisis
    ├── data/                 # Datasets de Austin Animal Center (Intakes y Outcomes)
    ├── notebooks/            # Notebooks de pruebas y exploración preliminar
    └── utilidades/           # Módulos Python auxiliares de limpieza y visualización