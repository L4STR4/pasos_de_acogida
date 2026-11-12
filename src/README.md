# 🐾 Análisis de Estancia y Adopción en Refugio de Animales (Austin Animal Center)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150k--records-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Mobile--First-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/Coste-0%20%E2%82%AC%20(Open%20Source)-brightgreen?style=for-the-badge)

## 📌 Descripción del Proyecto
Este proyecto de **Análisis Exploratorio de Datos (EDA)** examina el histórico de más de 150.000 entradas y salidas del **Austin Animal Center** (Texas, EE. UU.)[cite: 3]. El objetivo principal es identificar qué factores condicionan el tiempo de permanencia (`Days_in_Shelter`) de las mascotas en el refugio para optimizar la gestión de jaulas, recursos sanitarios y campañas de adopción.

Además, el proyecto cuenta con una **aplicación web responsive (Mobile-First)** enlazada mediante un **código QR** en la presentación oral para consultar métricas en tiempo real y datos curiosos sobre la adopción.

---

## 🎯 Hipótesis Analizadas (Mito vs. Realidad)

1. **El "Síndrome del Perro Negro":** ¿Tienen los perros de pelaje oscuro tiempos de estancia significativamente superiores en jaula?
2. **Estacionalidad y Camadas:** ¿Se produce la mayor saturación del refugio en agosto por vacaciones o se anticipa a mayo/junio por el nacimiento masivo de camadas sin esterilizar?
3. **Triaje y Salud al Ingreso:** ¿Los animales que ingresan heridos o enfermos son eutanasiados o se derivan mediante redes de traslado (*Transfer*)?
4. **Perros vs. Gatos:** ¿Quién pasa más tiempo de mediana encerrado antes de encontrar un hogar?

---

## 📊 Principales Hallazgos (Insights Clave)

* **Mediana de estancia:** El 50% de las mascotas salen en menos de **5,84 días**, aunque existen casos extremos (*outliers*) que superan los 1.000 días.
* **El efecto estacional:** El volumen de ingresos se dispara en **mayo (16.044)** y **junio (15.634)** debido a la *kitten season* (camadas estivales), exigiendo lanzar campañas de acogida preventiva en marzo/abril.
* **Diferencia de pelaje:** La brecha de mediana entre perros negros y claros es de apenas **+0,38 días (~9 horas)**, pero acumula más de 11.800 días de estancia adicional en la población total.
* **Puente socioeducativo con España:** Frente a la alta rotación de Austin (mediana de 6 días), las protectoras en España enfrentan estancias medias de **8 a 12 meses** para perros adultos (según datos de la Fundación Affinity).

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Procesamiento de Datos:** `Pandas`, `NumPy`
* **Visualización:** `Matplotlib`, `Seaborn`
* **Web Interactiva / Mobile:** `Streamlit`
* **Despliegue y Hosting:** GitHub Pages / Streamlit Community Cloud (Gratuito)

---

## 📁 Estructura del Repositorio

```text
proyecto-eda-mascotas/
├── README.md                 # Descripción ejecutiva del proyecto
├── requirements.txt          # Dependencias de librerías
└── src/
    ├── main.ipynb            # Notebook ejecutable con el flujo analítico completo
    ├── app.py                # Aplicación interactiva web/móvil
    ├── data/                 # Datasets procesados de Austin Animal Center
    ├── notebooks/            # Pruebas en sucio y exploración preliminar
    └── utils/                # Módulos auxiliares Python (limpieza y visualización)
    └── MEMORIA PROYECTO      # Memoria tecnica del proyecto