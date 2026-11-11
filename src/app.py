import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# ---------------------------------------------------------
# Configuración inicial de la página (Mobile-First)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Pasos a la Adopción",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed"  # Abre la app cerrada con el botón de las 3 rayas
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
        padding: 18px 16px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(6, 78, 59, 0.15);
    }
    .app-header h1 {
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 1.8rem;
        margin: 0;
    }
    
    /* Tarjetas */
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
    .card-contact {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        padding: 14px;
        border-radius: 10px;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER Y LOGO PERSONALIZADO
# ---------------------------------------------------------
ruta_logo = os.path.join(os.path.dirname(__file__), 'img', 'logo_app.png')

col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
with col_img2:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    else:
        st.image("https://img.icons8.com/color/180/pets.png", width=120)

st.markdown("""
    <div class="app-header">
        <h1>🐾 PASOS A LA ADOPCIÓN</h1>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# MENÚ NAVEGADOR MÓVIL (Con Perro 🐕 y Gato 🐈)
# ---------------------------------------------------------
st.sidebar.markdown("## 🐕 🐈 Pasos a la Adopción")
st.sidebar.caption("Toca una opción para navegar:")

opcion = st.sidebar.radio(
    "Menú principal:",
    [
        "🏠 1. Inicio / La Idea",
        "📊 2. EDA Austin (Hipótesis)",
        "🇪🇸 3. Estudio Affinity (España)",
        "🏘️ 4. Protectoras en España",
        "🔮 5. Simulador de Estancia (ML)"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Pasos a la Adopción v1.0")

# =========================================================
# OPCIÓN 1: INICIO Y PROPÓSITO DEL PROYECTO
# =========================================================
if opcion == "🏠 1. Inicio / La Idea":
    st.subheader("📌 ¿De qué va este proyecto?")
    
    st.markdown("""
    <div class="card-teal">
        <h4>🐾 Una mirada diferente a la adopción animal</h4>
        <p>¡Hola! <b>Pasos a la Adopción</b> nace con una idea muy clara: utilizar los datos para entender qué ocurre realmente en los refugios y buscar formas prácticas de echar una mano.</p>
        <p>A través de esta app móvil queremos explorar cómo influyen aspectos como el pelaje, la época del año o el estado de salud en el tiempo que una mascota pasa en una jaula. Además, conectamos estos datos con la realidad de las protectoras en España para dar visibilidad a su labor y facilitar el contacto con ellas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Navegación:** Pulsa sobre el **botón con las tres rayas (☰)** en la esquina superior izquierda para desplegar el menú de opciones.")

# =========================================================
# OPCIÓN 2: EDA AUSTIN (HIPÓTESIS)
# =========================================================
elif opcion == "📊 2. EDA Austin (Hipótesis)":
    st.subheader("📊 Análisis del Austin Animal Center")
    st.write("Explora las 4 hipótesis analizadas sobre más de 156.000 registros:")
    
    hipo = st.selectbox(
        "Elige una hipótesis:",
        [
            "H1: El Síndrome del Perro Negro",
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
        st.success("**Conclusión:** La diferencia en mediana es de solo **+0,38 días (~9 horas)**. Desmitificado el rechazo individual abrumador, aunque en la población total suma más de 11.800 días extra en jaula.")
        
    elif "H2" in hipo:
        st.markdown("#### ☀️ H2: Estacionalidad (Kitten Season)")
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        ingresos = [10805, 9792, 11895, 12383, 16044, 15634, 14343, 13891, 13557, 14668, 12159, 10870]
        fig = px.line(x=meses, y=ingresos, markers=True, color_discrete_sequence=['#064E3B'],
                      title="Ingresos Mensuales en el Refugio")
        st.plotly_chart(fig, use_container_width=True)
        st.warning("**Conclusión:** El colapso ocurre en **Mayo (16.044)** y **Junio (15.634)** por nacimientos de camadas descontroladas (*Kitten Season*), no por vacaciones en agosto.")
        
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
        st.info("**Conclusión:** Refutado. El centro opera como triaje: el 33,1% de enfermos y 61,5% de lactantes se derivan a protectoras externas (*Transfer*).")
        
    elif "H4" in hipo:
        st.markdown("#### 🐱 vs 🐶 H4: Perros vs. Gatos")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Gatos (Cat)", "7,12 Días", "Mediana Estancia")
        with col2:
            st.metric("Perros (Dog)", "5,78 Días", "Mediana Estancia")
        st.info("**Conclusión:** Los gatos permanecen 1,34 días más de mediana debido a la incubación requerida para las camadas lactantes de primavera.")

# =========================================================
# OPCIÓN 3: ESTUDIO FUNDACIÓN AFFINITY (ESPAÑA)
# =========================================================
elif opcion == "🇪🇸 3. Estudio Affinity (España)":
    st.subheader("🇪🇸 Estudio Fundación Affinity")
    st.caption("Resumen interactivo del informe 'Él nunca lo haría' (Datos en España)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Recogidos / Año", "285.720", "169k perros / 116k gatos")
    with col2:
        st.metric("Adopciones 2025", "42,9%", "-18% en perros este año")
        
    st.markdown("""
    <div class="card-highlight">
        <h4>📊 Datos Reales del Informe Oficial:</h4>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🆔 1. El grave problema de la falta de Microchip", expanded=True):
        st.write("""
        * **El 75% de los animales ingresados NO llevan microchip**, pese a ser obligatorio por ley.
        * Sin embargo, cuando un animal está identificado, el **65,2% regresa felizmente con su familia**. El chip transforma una pérdida temporal en una devolución en 48 horas.
        """)

    with st.expander("⏱️ 2. Permanencia en Chenil: Austin vs. España"):
        st.write("""
        * Mientras en Austin (EE. UU.) la mediana de estancia es de **5,8 días**, en España un perro adulto pasa de media entre **8 y 12,8 meses** en la protectora.
        * Los perros sénior (>8 años) superan los **13,2 meses** de estancia media.
        """)

    with st.expander("🚫 3. Principales Motivos de Abandono"):
        st.write("""
        1. **Camadas no deseadas (15,3%):** Causa #1 de abandono por falta de esterilización.
        2. **Pérdida de interés (14,0%):** Abandono por falta de compromiso.
        3. **Cambio de domicilio (11,9%):** Solo el **5% de los pisos en alquiler** admiten mascotas expresamente.
        """)

# =========================================================
# OPCIÓN 4: PROTECTORAS EN ESPAÑA CON CONTACTOS
# =========================================================
elif opcion == "🏘️ 4. Protectoras en España":
    st.subheader("🏘️ Directorio de Protectoras y Contacto")
    st.write("Consulta entidades de acogida y adopción en España con teléfono y datos directos de contacto:")
    
    zona = st.selectbox(
        "Selecciona zona geográfica:",
        [
            "Ámbito Estatal",
            "Comunidad de Madrid",
            "Cataluña",
            "Andalucía",
            "Comunidad Valenciana",
            "Norte (Galicia / País Vasco)"
        ]
    )
    
    if zona == "Ámbito Estatal":
        st.markdown("""
        <div class="card-contact">
            <h4>🏢 Fundación Affinity</h4>
            <p>📞 <b>Teléfono:</b> 93 495 80 00<br>
            🌐 <b>Web:</b> <a href="https://www.fundacion-affinity.org/" target="_blank">fundacion-affinity.org</a><br>
            📍 <b>Ámbito:</b> Investigación y estudio del abandono.</p>
        </div>
        <div class="card-contact">
            <h4>🐕 FAADA (Fundación para la Adopción)</h4>
            <p>📞 <b>Teléfono:</b> 93 624 55 38<br>
            🌐 <b>Web:</b> <a href="https://faada.org/" target="_blank">faada.org</a><br>
            ✉️ <b>Contacto:</b> info@faada.org</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif zona == "Comunidad de Madrid":
        st.markdown("""
        <div class="card-contact">
            <h4>🐕 Asociación ALBA (Madrid)</h4>
            <p>📞 <b>Teléfono / WhatsApp:</b> 609 29 19 23<br>
            🌐 <b>Web:</b> <a href="https://albaonline.org/" target="_blank">albaonline.org</a><br>
            📍 <b>Ubicación:</b> Camarma de Esteruelas, Madrid</p>
        </div>
        <div class="card-contact">
            <h4>🏛️ CIAAM (Comunidad de Madrid)</h4>
            <p>📞 <b>Teléfono:</b> 91 846 75 40<br>
            🌐 <b>Web:</b> <a href="https://www.comunidad.madrid/" target="_blank">comunidad.madrid</a></p>
        </div>
        """, unsafe_allow_html=True)
        
    elif zona == "Cataluña":
        st.markdown("""
        <div class="card-contact">
            <h4>🐈 SPAM (Protectora de Mataró)</h4>
            <p>📞 <b>Teléfono:</b> 93 756 60 26<br>
            🌐 <b>Web:</b> <a href="https://www.protectoramataró.org/" target="_blank">protectoramataró.org</a></p>
        </div>
        <div class="card-contact">
            <h4>🏛️ CAACB Barcelona</h4>
            <p>📞 <b>Teléfono:</b> 93 428 01 25<br>
            🌐 <b>Web:</b> <a href="https://ajuntament.barcelona.cat/proteccioanimals/es" target="_blank">ajuntament.barcelona.cat</a></p>
        </div>
        """, unsafe_allow_html=True)
        
    elif zona == "Andalucía":
        st.markdown("""
        <div class="card-contact">
            <h4>🐕 Galgos del Sur (Córdoba)</h4>
            <p>📞 <b>Teléfono:</b> 616 41 85 82<br>
            🌐 <b>Web:</b> <a href="https://galgosdelsur.es/" target="_blank">galgosdelsur.es</a></p>
        </div>
        <div class="card-contact">
            <h4>🐾 SPAPM (Protectora de Málaga)</h4>
            <p>📞 <b>Teléfono:</b> 952 43 45 00<br>
            🌐 <b>Web:</b> <a href="https://protectoramalaga.org/" target="_blank">protectoramalaga.org</a></p>
        </div>
        """, unsafe_allow_html=True)
        
    elif zona == "Comunidad Valenciana":
        st.markdown("""
        <div class="card-contact">
            <h4>🐕 Asoka El Grande (Alicante)</h4>
            <p>📞 <b>Teléfono:</b> 625 58 95 23<br>
            🌐 <b>Web:</b> <a href="https://asokaelgrande.org/" target="_blank">asokaelgrande.org</a></p>
        </div>
        <div class="card-contact">
            <h4>🐾 SVPAP (Valencia)</h4>
            <p>📞 <b>Teléfono:</b> 96 384 41 09<br>
            🌐 <b>Web:</b> <a href="https://svpap.com/" target="_blank">svpap.com</a></p>
        </div>
        """, unsafe_allow_html=True)
        
    elif zona == "Norte (Galicia / País Vasco)":
        st.markdown("""
        <div class="card-contact">
            <h4>🏛️ Refugio de Bando (Santiago de Compostela)</h4>
            <p>📞 <b>Teléfono:</b> 981 57 59 57<br>
            🌐 <b>Web:</b> <a href="https://refugiodebando.org/" target="_blank">refugiodebando.org</a></p>
        </div>
        <div class="card-contact">
            <h4>🐾 APA SOS Bilbao (Bizkaia)</h4>
            <p>📞 <b>Teléfono / WhatsApp:</b> 688 63 94 88<br>
            🌐 <b>Web:</b> <a href="https://www.apa-sosbilbao.net/" target="_blank">apa-sosbilbao.net</a></p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# OPCIÓN 5: SIMULADOR DE ESTANCIA (MACHINE LEARNING)
# =========================================================
elif opcion == "🔮 5. Simulador de Estancia (ML)":
    st.subheader("🔮 Simulador de Estancia Estimada")
    st.write("Selecciona los atributos de una mascota para estimar su tiempo de jaula:")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        especie_sim = st.selectbox("Especie", ["Perro 🐕", "Gato 🐈"])
        edad_sim = st.select_slider("Edad", ["Cachorro", "Joven", "Adulto", "Senior"])
    with col_s2:
        pelaje_sim = st.selectbox("Pelaje", ["Negro / Oscuro", "Claro / Otros"])
        salud_sim = st.selectbox("Salud al ingresar", ["Normal", "Herido / Enfermo"])
        
    dias_est = 5.5
    if especie_sim == "Gato 🐈":
        dias_est += 1.3
    if pelaje_sim == "Negro / Oscuro":
        dias_est += 0.4
    if edad_sim in ["Adulto", "Senior"]:
        dias_est += 3.5
    if salud_sim == "Herido / Enfermo":
        dias_est += 4.0
        
    st.markdown(f"""
    <div class="card-highlight">
        <h3>⏱️ Estancia estimada: <b>{dias_est:.1f} días</b></h3>
        <p><i>Estimación basada en la mediana histórica del dataset.</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.caption("📌 **Nota:** Este simulador servirá de base para el futuro modelo predictivo de Machine Learning.")