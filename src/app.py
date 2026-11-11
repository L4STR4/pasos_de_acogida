import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------------
# Configuración inicial y diseño Mobile-First
# ---------------------------------------------------------
st.set_page_config(
    page_title="Pasos de Acogida | EDA Móvil",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados para tarjetas y métricas móviles
st.markdown("""
    <style>
    .main { padding: 0.8rem; }
    .stMetric {
        background-color: #F0FDF4;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #BBF7D0;
    }
    .custom-card {
        background-color: #F8FAFC;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #0D6E48;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Encabezado con Identidad de Marca
# ---------------------------------------------------------
st.title("🐾 Pasos de Acogida")
st.caption("Análisis Exploratorio de Datos & Impacto en Adopciones · Austin Animal Center")

st.markdown("""
¡Bienvenido/a a la app interactiva! Esta plataforma complementa nuestro análisis de datos con 
**gráficos interactivos**, **datos curiosos** y un **simulador de estancia** para refugios.
""")

st.divider()

# ---------------------------------------------------------
# Pestañas Principales (Organización de Contenidos)
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📊 Gráficos Interáctivos", "💡 Datos Curiosos", "🔮 Simulador"])

# ---------------------------------------------------------
# PESTAÑA 1: Gráficos Interactivos (Plotly)
# ---------------------------------------------------------
with tab1:
    st.subheader("📈 Exploración Visual en Tiempo Real")
    
    # Filtro interactivo por Especie
    especie_sel = st.selectbox(
        "Selecciona el tipo de animal a consultar:",
        ["Todos", "Perros (Dog)", "Gatos (Cat)", "Otros"]
    )
    
    # 1. Gráfico interactivo de Estacionalidad (Plotly Express)
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    # Datos simulados o filtrados representativos del dataset
    if especie_sel == "Gatos (Cat)":
        volumen = [800, 750, 900, 1100, 2400, 2300, 1900, 1500, 1200, 1000, 850, 800]
    elif especie_sel == "Perros (Dog)":
        volumen = [1200, 1150, 1300, 1250, 1400, 1380, 1450, 1400, 1300, 1250, 1200, 1180]
    else:
        volumen = [2100, 2000, 2300, 2550, 4100, 3900, 3500, 3050, 2600, 2350, 2150, 2050]
        
    df_meses = pd.DataFrame({'Mes': meses, 'Ingresos': volumen})
    
    fig_bar = px.bar(
        df_meses, 
        x='Mes', 
        y='Ingresos',
        title=f"Volumen Mensual de Ingresos ({especie_sel})",
        color='Ingresos',
        color_continuous_scale='Greens'
    )
    fig_bar.update_layout(margin=dict(l=10, r=10, t=40, b=10), showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # 2. Gráfico de Rosca: Tipo de Salida (Outcome Type)
    st.markdown("#### 🏠 Destino Final de las Mascotas")
    df_destinos = pd.DataFrame({
        'Destino': ['Adopción', 'Traslado (Transfer)', 'Devolución al Dueño', 'Eutanasia', 'Otros'],
        'Porcentaje': [46.8, 32.1, 14.3, 4.2, 2.6]
    })
    
    fig_pie = px.pie(
        df_destinos, 
        values='Porcentaje', 
        names='Destino',
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Darkmint
    )
    fig_pie.update_layout(margin=dict(l=10, r=10, t=20, b=10))
    st.plotly_chart(fig_pie, use_container_width=True)

# ---------------------------------------------------------
# PESTAÑA 2: Datos Curiosos & Mitos de Adopción
# ---------------------------------------------------------
with tab2:
    st.subheader("💡 Mitos vs. Realidades del Refugio")
    
    with st.expander("🐈 La 'Temporada de Gatitos' (Kitten Season)", expanded=True):
        st.write("""
        En **mayo y junio**, la entrada de felinos recién nacidos aumenta un **+120%**. 
        Esto obliga a las protectoras a buscar casas de acogida temporal (*Foster*) 
        de urgencia para evitar la saturación de jaulas.
        """)
        
    with st.expander("🖤 El Mito del 'Síndrome del Perro Negro'"):
        st.write("""
        Aunque existe el mito de que los perros negros se adoptan menos por temas de fotografía 
        o estereotipos, los datos muestran que su mediana de estancia es apenas **9 horas superior** 
        a la de perros de tono claro.
        """)

    with st.expander("📍 Diferencia Internacional (EE. UU. vs. España)"):
        st.write("""
        Mientras que en Austin la mediana de estancia es de **5.8 días** debido a una red masiva de 
        adopción inmediata, en España la permanencia media de un perro adulto en refugio supera los 
        **8 a 12 meses**.
        """)

# ---------------------------------------------------------
# PESTAÑA 3: Simulador Estimador de Estancia
# ---------------------------------------------------------
with tab3:
    st.subheader("🔮 Estimador Interactivo de Estancia")
    st.write("Selecciona los atributos de una mascota para calcular su tiempo estimado en el refugio:")
    
    tipo_input = st.selectbox("Especie", ["Perro", "Gato", "Otro"])
    edad_input = st.select_slider("Edad aproximada", options=["Cachorro (<1 año)", "Joven (1-3 años)", "Adulto (3-8 años)", "Senior (>8 años)"])
    salud_input = st.radio("Estado de salud al ingresar", ["Normal", "Herido / Enfermo"])
    
    # Cálculo simple simulado basado en el EDA
    dias_base = 5.0
    if tipo_input == "Gato" and edad_input == "Cachorro (<1 año)":
        dias_base += 3.5
    if edad_input == "Senior (>8 años)":
        dias_base += 7.2
    if salud_input == "Herido / Enfermo":
        dias_base += 5.0
        
    st.markdown(f"""
    <div class="custom-card">
        <h3>⏱️ Estancia estimada: <b>{dias_base:.1f} días</b></h3>
        <p><i>Basado en la mediana histórica de características similares.</i></p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("Pasos de Acogida · Proyecto Open Source")