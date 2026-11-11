import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# ---------------------------------------------------------
# Configuración inicial de la página (Mobile-First)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Pasos a la Adopción | App Móvil",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="expanded"
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
        padding: 22px 16px;
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
# BANNER SUPERIOR CON IMAGEN MODIFICABLE DE CABECERA
# ---------------------------------------------------------
# Si quieres usar una imagen tuya local, pon tu archivo en src/img/portada.jpg
ruta_imagen_local = os.path.join(os.path.dirname(__file__), 'img', 'portada.jpg')

if os.path.exists(ruta_imagen_local):
    st.image(ruta_imagen_local, use_container_width=True)
else:
    # Imagen por defecto desde URL (Modificable fácilmente cambiando el enlace)
    st.image(
        "https://images.unsplash.com/photo-1548767797-d8c844163c4c?q=80&w=1000&auto=format&fit=crop",
        use_container_width=True,
        caption="Pasos a la Adopción · Proyecto Data Science & Concienciación Social"
    )

st.markdown("""
    <div class="app-header">
        <h1>🐾 PASOS A LA ADOPCIÓN</h1>
        <p>Análisis de Datos, Concienciación Social y Entorno Interactivo</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# MENÚ NAVEGADOR MÓVIL (Con Perro 🐕 y Gato 🐈)
# ---------------------------------------------------------
st.sidebar.markdown("## 🐕 🐈 Pasos a la Adopción")
st.sidebar.caption("Menú Principal de Navegación")

opcion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "🏠 1. Inicio / La Idea",
        "📊 2. EDA Austin (Hipótesis)",
        "🇪🇸 3. Estudio Affinity (España)",
        "🏘️ 4. Protectoras en España"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Proyecto Open Source · Data Analyst Bootcamp")

# =========================================================
# OPCIÓN 1: INICIO, PROPÓSITO Y SIMULADOR
# =========================================================
if opcion == "🏠 1. Inicio / La Idea":
    st.subheader("📌 Sobre el Proyecto")
    
    st.markdown("""
    <div class="card-teal">
        <h4>¿Cuál es la idea de este proyecto?</h4>
        <p>Unir el <b>Análisis Exploratorio de Datos (EDA)</b> con una causa social: estudiar los factores que provocan que los animales queden estancados en refugios para optimizar su gestión, acelerar la adopción y sensibilizar a la sociedad.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # REEMPLAZO: Simulador de Estancia en lugar de métricas de análisis
    st.subheader("🔮 Simulador Interactivo de Estancia")
    st.write("Selecciona las características de una mascota para estimar su tiempo medio de permanencia en el refugio:")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        especie_sim = st.selectbox("Especie", ["Perro 🐕", "Gato 🐈"])
        edad_sim = st.select_slider("Edad", ["Cachorro", "Joven", "Adulto", "Senior"])
    with col_s2:
        pelaje_sim = st.selectbox("Pelaje", ["Negro / Oscuro", "Claro / Otros"])
        salud_sim = st.selectbox("Salud al ingresar", ["Normal", "Herido / Enfermo"])
        
    # Lógica simple de simulación basada en la mediana del EDA
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
        <p><i>Estimación basada en la mediana histórica de características similares en el refugio.</i></p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# OPCIÓN 2: EDA AUSTIN (HIPÓTESIS)
# =========================================================
elif opcion == "📊 2. EDA Austin (Hipótesis)":
    st.subheader("📊 Análisis de Hipótesis (Austin Animal Center)")
    st.write("Selecciona una hipótesis para explorar sus datos y conclusiones:")
    
    hipo = st.selectbox(
        "Elige la hipótesis:",
        [
            "H1: Síndrome del Perro Negro",
            "H2: Estacionalidad y Camadas Estivales",
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
        st.success("**Conclusión:** La diferencia es de solo +0,38 días (~9 horas) en mediana. Desmitificado a nivel individual, aunque en el acumulado total representa más de 11.800 días de jaula extra.")
        
    elif "H2" in hipo:
        st.markdown("#### ☀️ H2: Estacionalidad (Kitten Season)")
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        ingresos = [10805, 9792, 11895, 12383, 16044, 15634, 14343, 13891, 13557, 14668, 12159, 10870]
        fig = px.line(x=meses, y=ingresos, markers=True, color_discrete_sequence=['#064E3B'],
                      title="Ingresos Mensuales en el Refugio")
        st.plotly_chart(fig, use_container_width=True)
        st.warning("**Conclusión:** El colapso arranca en Mayo (16.044) y Junio (15.634) debido al nacimiento descontrolado de camadas sin esterilizar.")
        
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
        st.info("**Conclusión:** Refutado. El centro deriva el 33,1% de enfermos y 61,5% de lactantes a protectoras y hospitales mediante traslados (Transfer).")
        
    elif "H4" in hipo:
        st.markdown("#### 🐱 vs 🐶 H4: Perros vs. Gatos")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Gatos (Cat)", "7,12 Días", "Mediana")
        with col2:
            st.metric("Perros (Dog)", "5,78 Días", "Mediana")
        st.info("**Conclusión:** Los gatos superan a los perros en 1,34 días de mediana debido a la incubación requerida para las camadas lactantes de primavera.")

# =========================================================
# OPCIÓN 3: ESTUDIO FUNDACIÓN AFFINITY (ESPAÑA)
# =========================================================
elif opcion == "🇪🇸 3. Estudio Affinity (España)":
    st.subheader("🇪🇸 La Realidad en España")
    st.caption("Datos oficiales extraídos del Informe 'Él nunca lo haría' (Fundación Affinity 2026)")[cite: 1]
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Abandonos / Año", "285.720", "Perros y Gatos")[cite: 1]
    with col2:
        st.metric("Caída Adopciones", "-18%", "En el último año")[cite: 1]
        
    st.markdown("""
    <div class="card-highlight">
        <h4>🚨 Hallazgos Críticos del Informe Affinity:</h4>
        <ul>
            <li><b>75% sin Microchip:</b> 3 de cada 4 animales ingresan sin identificar a los refugios españoles[cite: 1].</li>
            <li><b>12,8 Meses:</b> Es la estancia media de un perro adulto en cheniles españoles (frente a los 5,8 días de Austin)[cite: 1, 3].</li>
            <li><b>15,3% Camadas No Deseadas:</b> Sigue siendo el motivo #1 de abandono en nuestro país[cite: 1, 4].</li>
            <li><b>Solo 5% de Alquileres admiten mascotas:</b> El cambio de domicilio se ha convertido en la tercera causa principal de abandono[cite: 4, 5].</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# OPCIÓN 4: PROTECTORAS EN ESPAÑA CON TELÉFONO Y CONTACTO
# =========================================================
elif opcion == "🏘️ 4. Protectoras en España":
    st.subheader("🏘️ Directorio de Protectoras y Contacto")
    st.write("Consulta entidades de acogida y adopción en España con teléfono y datos directos de contacto:")
    
    zona = st.selectbox(
        "Filtra por zona geográfica:",
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
            📍 <b>Ámbito:</b> Investigación y concienciación nacional.</p>
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
            🌐 <b>Web:</b> <a href="https://www.comunidad.madrid/" target="_blank">comunidad.madrid</a><br>
            📍 <b>Ubicación:</b> Colmenar Viejo, Madrid</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif zona == "Cataluña":
        st.markdown("""
        <div class="card-contact">
            <h4>🐈 SPAM (Protectora de Mataró)</h4>
            <p>📞 <b>Teléfono:</b> 93 756 60 26<br>
            🌐 <b>Web:</b> <a href="https://www.protectoramataró.org/" target="_blank">protectoramataró.org</a><br>
            ✉️ <b>Contacto:</b> info@protectoramataró.org</p>
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
            <h4>🐕 Asociación Galgos del Sur (Córdoba)</h4>
            <p>📞 <b>Teléfono:</b> 616 41 85 82<br>
            🌐 <b>Web:</b> <a href="https://galgosdelsur.es/" target="_blank">galgosdelsur.es</a><br>
            ✉️ <b>Contacto:</b> contacto@galgosdelsur.es</p>
        </div>
        <div class="card-contact">
            <h4>🐾 SPAPM (Protectora de Málaga)</h4>
            <p>📞 <b>Teléfono:</b> 952 43 45 00<br>
            🌐 <b>Web:</b> <a href="https://protectoramaga.org/" target="_blank">protectoramalaga.org</a></p>
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

    with st.expander("🤝 ¿Cómo colaborar con estas entidades?"):
        st.write("""
        1. **Adopción Responsable:** Contacta directamente a los teléfonos indicados para solicitar cita previa.
        2. **Acogida Temporal (*Foster*):** Imparable ayuda para cachorros sin vacunar o animales convalecientes.
        3. **Voluntariado y Paseos:** Apoyo en paseos de fin de semana para animales en cheniles.
        """)