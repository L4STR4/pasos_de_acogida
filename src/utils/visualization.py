import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid")

def graficar_estancia_por_especie(df: pd.DataFrame):
    # Filtrar las especies principales
    df_filtrado = df[df['Animal Type'].isin(['Dog', 'Cat', 'Bird', 'Other'])]
    
    plt.figure(figsize=(11, 6))
    
    # showfliers=True (o simplemente omitirlo) hace que se dibujen todos los outliers.
    # Con flierprops les damos formato rojo semitransparente para destacarlos.
    ax = sns.boxplot(
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
    
    plt.title("Distribución de Días de Estancia por Especie (Outliers Visibles)", fontsize=13, pad=12, fontweight='bold')
    plt.xlabel("Especie", fontsize=11)
    plt.ylabel("Días de Estancia en Refugio", fontsize=11)
    
    # Guardar copia en alta resolución para la memoria / presentación
    plt.savefig('estancia_por_especie_outliers.png', dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.show()