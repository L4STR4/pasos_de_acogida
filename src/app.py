import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------------------------------------------------
# Configuración inicial de la página (Mobile-First)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Pasos a la Adopción | App Móvil",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="expanded" # Abre el menú por defecto
)

# ---------------------------------------------------------
# Estilos CSS Personalizados (Montserrat + Verde Petróleo)
# ---------------------------------------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Header Principal */
    .app-header {
        background-color: #064E3B;
        color: #FFFFFF;
        padding: 20px 16px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(6, 78, 59, 0.15);
    }
    .app-header h1 {
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 1.8rem;
        margin-bottom: 4px;
    }
    .app-header p {
        color: #A7F3D0 !important;
        font-size: 0.9rem;
        margin-bottom: 0;
    }
    
    /* Tarjetas de Estilo */
    .card-teal {
        background-color: #F8FAFC;
        border-left: 6px solid #064E3B;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 16px;
    }
    .card-highlight {
        background-color: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-left: 6px solid #0D6E48;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 16px;
    }
    
    /* Métricas estilizadas */
    .stMetric {
        background-color: #F0FDF4;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #A7F3D0;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Header Fijo de la App Móvil
# ---------------------------------------------------------
st.markdown("""
    <div class="app-header">
        <h1>🐾 PASOS A LA ADOPCIÓN</h1>
        <p>App Móvil del Proyecto · EDA & Impacto Social</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# MENÚ NAVEGADOR MÓVIL (Barra Lateral / Selector)
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/pets.png", width=60)
st.sidebar.title("📱 Menú de Navegación")

opcion = st.sidebar.radio(
    "Selecciona una opción:",
    [
        "🏠 1. Inicio / La Idea",
        "🇪🇸 2. Estudio Affinity (España)",
        "📊 3. EDA Austin (Hipótesis)",
        "🏘️ 4. Protectoras en España",
        "🔮 5. Simulador ML (Futuro)"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Pasos a la Adopción v1.0 · Open Source")

# =========================================================
# OPCIÓN 1: INICIO Y PROPÓSITO
# =========================================================
if opcion == "🏠 1. Inicio / La Idea":
    st.subheader("📌 Sobre el Proyecto")
    
    st.markdown("""
    <div class="card-teal">
        <h4>¿Cuál es la idea de este proyecto?</h4>
        <p>Unir el <b>Análisis Exploratorio de Datos (EDA)</b> con la concienciación social sobre el abandono animal. Estudiamos los factores que retienen a los animales en refugios para proponer soluciones operativas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Cifras Clave del Análisis")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Dataset Austin", "156.041", "Registros analizados")
    with col2:
        st.metric("Estancia Mediana", "5,8 Días", "En Austin (EE.UU.)")

# =========================================================
# OPCIÓN 2: ESTUDIO FUNDACIÓN AFFINITY (ESPAÑA)
# =========================================================
elif opcion == "🇪🇸 2. Estudio Affinity (España)":
    st.subheader("🇪🇸 La Realidad en España")
    st.caption("Datos oficiales extraídos del Estudio 'Él nunca lo haría' (Fundación Affinity 2026)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Abandonos / Año", "285.720", "Perros y Gatos")
    with col2:
        st.metric("Caída Adopciones", "-18%", "En el último año")
        
    st.markdown("""
    <div class="card-highlight">
        <h4>🚨 Hallazgos Críticos del Informe:</h4>
        <ul>
            <li><b>75% sin Microchip:</b> 3 de cada 4 animales entran sin identificar a los refugios españoles.</li>
            <li><b>12,8 Meses:</b> Es la estancia media de un perro adulto en protectoras españolas (frente a los 5,8 días de Austin).</li>
            <li><b>15,3% Camadas No Deseadas:</b> Sigue siendo el motivo #1 de abandono en nuestro país.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# OPCIÓN 3: EXPLORADOR DE HIPÓTESIS (EDA AUSTIN)
# =========================================================
elif opcion == "📊 3. EDA Austin (Hipótesis)":
    st.subheader("📊 Análisis de Hipótesis (Austin EDA)")
    st.write("Toca en el selector para ver la gráfica y resolución de cada hipótesis:")
    
    hipo = st.selectbox(
        "Elige la hipótesis:",
        [
            "H1: Síndrome del Perro Negro",
            "H2: Estacionalidad (Kitten Season)",
            "H3: Triaje de Salud vs. Eutanasia",
            "H4: Perros vs. Gatos"
        ]
    )
    
    st.divider()
    
    if "H1" in hipo:
        st.markdown("#### 🖤 H1: El Síndrome del Perro Negro")
        df_pelaje = pd.DataFrame({
            'Pelaje': ['Negro / Oscuro', 'Claro / Otros'],
            'Mediana_Dias': [5.90, 5.52]
        })
        fig = px.bar(df_pelaje, x='Pelaje', y='Mediana_Dias', text='Mediana_Dias',
                     color='Pelaje', color_discrete_sequence=['#064E3B', '#34D399'],
                     title="Mediana de Días de Estancia por Pelaje")
        fig.update_traces(texttemplate='%{text:.2f} días', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
        st.success("**Resolución:** Diferencia de solo +0,38 días (~9 horas). Desmitificado a nivel individual, aunque acumula +11.800 días extra en la población total.")
        
    elif "H2" in hipo:
        st.markdown("#### ☀️ H2: Estacionalidad (Kitten Season)")
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        ingresos = [10805, 9792, 11895, 12383, 16044, 15634, 14343, 13891, 13557, 14668, 12159, 10870]
        fig = px.line(x=meses, y=ingresos, markers=True, color_discrete_sequence=['#064E3B'],
                      title="Ingresos Mensuales en el Refugio")
        st.plotly_chart(fig, use_container_width=True)
        st.warning("**Resolución:** Picos críticos en Mayo (16k) y Junio (15,6k) por nacimientos estivales. Exige preparar la red de acogidas en marzo/abril.")
        
    elif "H3" in hipo:
        st.markdown("#### 🏥 H3: Triaje de Salud vs. Eutanasia")
        df_salud = pd.DataFrame({
            'Estado': ['Normal', 'Herido', 'Enfermo', 'Lactante'],
            'Adopción %': [50.7, 29.4, 20.7, 30.0],
            'Traslado %': [27.1, 26.5, 33.1, 61.5],
            'Eutanasia %': [3.5, 26.8, 34.6, 2.4]
        }).melt(id_vars='Estado', var_name='Destino', value_name='Porcentaje')
        fig = px.bar(df_salud, x='Estado', y='Porcentaje', color='Destino', barmode='group',
                     color_discrete_sequence=['#064E3B', '#34D399', '#D97706'])
        st.plotly_chart(fig, use_container_width=True)
        st.info("**Resolución:** Refutado. El centro opera como triaje: el 33,1% de enfermos y 61,5% de lactantes se traslada a protectoras especializadas.")
        
    elif "H4" in hipo:
        st.markdown("#### 🐱 vs 🐶 H4: Perros vs. Gatos")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Gatos (Cat)", "7,12 Días", "Mediana")
        with col2:
            st.metric("Perros (Dog)", "5,78 Días", "Mediana")
        st.info("**Resolución:** Los gatos pasan 1,34 días más de mediana debido a la incubación de camadas lactantes.")

# =========================================================
# OPCIÓN 4: DIRECTORIO DE PROTECTORAS EN ESPAÑA
# =========================================================
elif opcion == "🏘️ 4. Protectoras en España":
    st.subheader("🏘️ Directorio de Protectoras y Ayuda")
    st.write("Consulta entidades de adopción en España por zona:")
    
    zona = st.selectbox(
        "Selecciona zona geográfica:",
        ["Ámbito Estatal", "Comunidad de Madrid", "Cataluña", "Andalucía", "C. Valenciana", "Norte (Galicia/País Vasco)"]
    )
    
    if zona == "Ámbito Estatal":
        st.markdown("""
        * **Fundación Affinity:** [fundacion-affinity.org](https://www.fundacion-affinity.org/)
        * **Miwuki Pet Center:** Plataforma nacional de adopción.
        * **FAADA:** [faada.org](https://faada.org/)
        """)
    elif zona == "Comunidad de Madrid":
        st.markdown("* **ALBA:** [albaonline.org](https://albaonline.org/)\n* **CIAAM Madrid**")
    elif zona == "Cataluña":
        st.markdown("* **SPAM Mataró:** [protectoramataró.org](https://www.protectoramataró.org/)\n* **CAACB Barcelona**")
    elif zona == "Andalucía":
        st.markdown("* **Galgos del Sur (Córdoba)**\n* **SPAPM Málaga**")
    elif zona == "C. Valenciana":
        st.markdown("* **SVPAP Valencia**\n* **Asoka El Grande (Alicante)**")
    elif zona == "Norte (Galicia/País Vasco)":
        st.markdown("* **Refugio de Bando (Santiago)**\n* **APA SOS Bilbao**")

# =========================================================
# OPCIÓN 5: SIMULADOR DE MACHINE LEARNING (FUTURO)
# =========================================================
elif opcion == "🔮 5. Simulador ML (Futuro)":
    st.subheader("🔮 Motor Predictivo (Machine Learning)")
    
    st.markdown("""
    <div class="card-highlight">
        <h4>🎯 El Planteamiento Futuro</h4>
        <p>Predecir en las primeras 24 horas de ingreso qué mascotas tienen riesgo de superar los 15 días en jaula para asignarles automáticamente familias de acogida pre-evaluadas sin pisar el chenil.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Simulador Interactivo de Riesgo")
    tipo = st.selectbox("Especie", ["Perro", "Gato"])
    salud = st.selectbox("Estado Sanitario", ["Normal", "Herido / Enfermo"])
    edad = st.select_slider("Edad", ["Cachorro", "Joven", "Adulto", "Senior"])
    
    if st.button("Calcular Riesgo Predictivo"):
        if salud != "Normal" or edad == "Senior":
            st.error("🚨 **Alto Riesgo de Permanencia Prolongada (>15 días).** Se sugiere activar campaña prioritaria.")
        else:
            st.success("✅ **Bajo Riesgo de Estancia.** Estancia estimada: 4 a 6 días.")