import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Configuración de la página (Optimizado para móvil)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Pasos de Acogida | EDA Móvil",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS para mejorar la legibilidad en pantallas móviles
st.markdown("""
    <style>
    .main {
        padding: 1rem;
    }
    .stMetric {
        background-color: #F0FDF4;
        padding: 12px;
        border-radius: 10px;
        border: 1px solid #BBF7D0;
    }
    .fact-card {
        background-color: #F8FAFC;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #0D6E48;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Encabezado Principal
# ---------------------------------------------------------
st.title("🐾 Pasos de Acogida")
st.caption("Análisis Exploratorio de Datos · Austin Animal Center")

st.markdown("""
Bienvenido/a a la app móvil del proyecto. Aquí podrás explorar los datos curiosos, 
métricas clave e historias detrás del análisis de estancias en protectoras.
""")

st.divider()

# ---------------------------------------------------------
# Sección 1: Métricas Clave (KPIs)
# ---------------------------------------------------------
st.subheader("📊 Métricas Clave de Estancia")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Mediana de Estancia", value="5.8 Días", delta="-12% vs Promedio")
with col2:
    st.metric(label="Tasa de Adopción", value="46.8%", delta="+3.2% este año")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sección 2: Datos Curiosos (Mito vs Realidad)
# ---------------------------------------------------------
st.subheader("💡 Datos Curiosos & Hallazgos")

with st.expander("🐈 1. La 'Temporada de Gatitos' (Kitten Season)"):
    st.markdown("""
    En **mayo y junio**, el volumen de entradas de gatos se incrementa en más de un **120%** 
    debido a las camadas estivales descontroladas. Esto satura las instalaciones antes de los meses de verano.
    """)

with st.expander("🐕 2. El 'Síndrome del Perro Negro': ¿Mito o Realidad?"):
    st.markdown("""
    En los datos analizados, la diferencia en la mediana de días de estancia entre perros negros 
    y perros de pelaje claro es de apenas **0.38 días (~9 horas)**. Sin embargo, al acumular miles 
    de registros, representa miles de días extra en jaula.
    """)

with st.expander("🌍 3. Austin vs. Protectoras en España"):
    st.markdown("""
    Mientras que en el Austin Animal Center la mediana de estancia es inferior a **6 días** 
    (gracias a una red intensiva de acogidas), en España la estancia media en refugios alcanza los 
    **8 a 12 meses** para un perro adulto.
    """)

st.divider()

# ---------------------------------------------------------
# Sección 3: Próximo Paso (Machine Learning)
# ---------------------------------------------------------
st.subheader("🚀 El Futuro del Proyecto")

st.markdown("""
<div class="fact-card">
<h4>🔮 Motor Predictivo de Riesgo de Estancia</h4>
Próximamente integraremos un modelo de <b>Machine Learning</b> para predecir desde el primer día 
de ingreso qué animales requerirán campañas prioritarias de acogida.
</div>
""", unsafe_allow_html=True)

# Pie de página
st.caption("Desarrollado con Streamlit · Gratuito y Open Source")