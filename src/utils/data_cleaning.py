import pandas as pd
import numpy as np

def cargar_y_limpiar_datos(ruta_intakes: str, ruta_outcomes: str) -> pd.DataFrame:
    # Cargar los CSVs de entradas y salidas de Austin
    intakes = pd.read_csv(ruta_intakes)
    outcomes = pd.read_csv(ruta_outcomes)
    
    # Formatear fechas para que Pandas no tire UserWarnings al adivinar el formato
    formato_fecha = '%m/%d/%Y %I:%M:%S %p'
    intakes['IntakeDate'] = pd.to_datetime(intakes['DateTime'], format=formato_fecha, errors='coerce')
    outcomes['OutcomeDate'] = pd.to_datetime(outcomes['DateTime'], format=formato_fecha, errors='coerce')
    
    # Ordenar por fecha antes de hacer el merge temporal
    intakes_sorted = intakes.sort_values('IntakeDate')
    outcomes_sorted = outcomes.sort_values('OutcomeDate')
    
    # Quedarme solo con las columnas que me valen de la salida
    cols_outcomes = [
        'Animal ID', 'OutcomeDate', 'Outcome Type', 
        'Outcome Subtype', 'Sex upon Outcome', 'Age upon Outcome'
    ]
    outcomes_sub = outcomes_sorted[cols_outcomes]
    
    # Emparejar cada entrada con su salida mas cercana en el tiempo
    df = pd.merge_asof(
        intakes_sorted,
        outcomes_sub,
        by='Animal ID',
        left_on='IntakeDate',
        right_on='OutcomeDate',
        direction='forward'
    )
    
    # Tirar registros que no tienen fecha de salida (siguen en el refugio)
    df = df.dropna(subset=['OutcomeDate']).copy()
    
    # Sacar los dias en el refugio dividiendo entre segundos de un dia
    df['Days_in_Shelter'] = (df['OutcomeDate'] - df['IntakeDate']).dt.total_seconds() / 86400.0
    
    # Sacar variables temporales para ver la estacionalidad
    df['Intake_Month'] = df['IntakeDate'].dt.month
    df['Intake_Year'] = df['IntakeDate'].dt.year
    df['Intake_DayOfWeek'] = df['IntakeDate'].dt.day_name()
    
    # Flag rapido para saber si el pelaje tiene color negro
    df['Is_Black'] = df['Color'].str.contains('Black', case=False, na=False)
    df['Color_Category'] = np.where(df['Is_Black'], 'Pelaje Negro', 'Otros Colores')
    
    return df


def obtener_resumen_kpis(df: pd.DataFrame) -> dict:
    # Resumen numerico directo para la presentacion
    kpis = {
        'total_registros': len(df),
        'mediana_dias_estancia': round(df['Days_in_Shelter'].median(), 2),
        'media_dias_estancia': round(df['Days_in_Shelter'].mean(), 2),
        'max_dias_estancia': round(df['Days_in_Shelter'].max(), 2),
        'tasa_adopcion_pct': round((df['Outcome Type'] == 'Adoption').mean() * 100, 2),
        'tasa_eutanasia_pct': round((df['Outcome Type'] == 'Euthanasia').mean() * 100, 2)
    }
    return kpis