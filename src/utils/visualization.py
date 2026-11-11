import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Asegurar que existe la carpeta para guardar las imágenes de la presentación
OS_IMG_DIR = os.path.join(os.path.dirname(__file__), '..', 'img')
os.makedirs(OS_IMG_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")


def graficar_estacionalidad_ingresos(df: pd.DataFrame):
    plt.figure(figsize=(10, 5))
    meses_etiquetas = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    
    ax = sns.countplot(data=df, x='Intake_Month', palette='Blues_d')
    ax.set_xticks(range(12))
    ax.set_xticklabels(meses_etiquetas)
    
    plt.title("Volumen Histórico de Ingresos por Mes", fontsize=13, pad=12, fontweight='bold')
    plt.xlabel("Mes de Ingreso", fontsize=11)
    plt.ylabel("Total de Animales", fontsize=11)
    
    ruta_guardado = os.path.join(OS_IMG_DIR, 'estacionalidad_ingresos.png')
    plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.show()


def graficar_comparativa_pelaje(df: pd.DataFrame):
    perros = df[df['Animal Type'] == 'Dog'].copy()
    
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(
        data=perros, 
        x='Color_Category', 
        y='Days_in_Shelter', 
        estimator=pd.Series.median, 
        errorbar=None, 
        palette=['#2C3E50', '#BDC3C7']
    )
    
    plt.title("Mediana de Días en Jaula: Perros Negros vs Resto", fontsize=13, pad=12, fontweight='bold')
    plt.xlabel("Categoría de Pelaje", fontsize=11)
    plt.ylabel("Mediana de Días de Estancia", fontsize=11)
    
    for p in ax.patches:
        ax.annotate(f"{p.get_height():.2f} días", 
                    (p.get_x() + p.get_width() / 2., p.get_height() / 2), 
                    ha='center', va='center', color='white', fontweight='bold', fontsize=11)
        
    ruta_guardado = os.path.join(OS_IMG_DIR, 'comparativa_pelaje_perros.png')
    plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.show()


def graficar_destinos_por_condicion(df: pd.DataFrame):
    top_condiciones = df['Intake Condition'].value_counts().head(5).index
    df_top = df[df['Intake Condition'].isin(top_condiciones)]
    
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df_top, x='Intake Condition', hue='Outcome Type', palette='Set2')
    
    plt.title("Tipo de Salida según la Condición de Salud al Ingreso", fontsize=13, pad=12, fontweight='bold')
    plt.xlabel("Estado de Salud al Entrar", fontsize=11)
    plt.ylabel("Cantidad de Registros", fontsize=11)
    plt.legend(title="Destino Final", bbox_to_anchor=(1.05, 1), loc='upper left')
    
    ruta_guardado = os.path.join(OS_IMG_DIR, 'destinos_por_condicion.png')
    plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.show()


def graficar_estancia_por_especie(df: pd.DataFrame):
    df_filtrado = df[df['Animal Type'].isin(['Dog', 'Cat', 'Bird', 'Other'])]
    
    plt.figure(figsize=(10, 5))
    sns.boxplot(
        data=df_filtrado, 
        x='Animal Type', 
        y='Days_in_Shelter', 
        showfliers=True, 
        palette='Pastel1',
        flierprops={
            'marker': 'o', 
            'markersize': 3, 
            'markerfacecolor': '#E74C3C', 
            'alpha': 0.4, 
            'markeredgecolor': 'none'
        }
    )
    
    plt.title("Días de Estancia por Especie", fontsize=13, pad=12, fontweight='bold')
    plt.xlabel("Especie", fontsize=11)
    plt.ylabel("Días en el Refugio", fontsize=11)
    
    ruta_guardado = os.path.join(OS_IMG_DIR, 'estancia_por_especie.png')
    plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.show()