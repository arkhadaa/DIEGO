import streamlit as st
import pandas as pd
from utils import get_data_from_api, preprocess_data

def app(df):  # Recibe df como argumento
    st.title("Interacción con los Datos")

    st.header("Mostrar Datos Originales")
    st.write(df)

    # Filtrar las columnas numéricas
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(columnas_numericas) == 0:
        st.warning("No se encontraron columnas numéricas para realizar el análisis.")
        return

    # Selección de columna para análisis
    columna_seleccionada = st.selectbox("Selecciona una columna numérica para analizar:", columnas_numericas)
    
    if columna_seleccionada:
        st.subheader(f"Estadísticas para {columna_seleccionada}:")
        st.write(f"Media: {df[columna_seleccionada].mean():,.2f}")
        st.write(f"Mediana: {df[columna_seleccionada].median():,.2f}")
        st.write(f"Desviación Estándar: {df[columna_seleccionada].std():,.2f}")
    
    # Selección de columna para ordenar
    columna_orden = st.selectbox("Selecciona una columna para ordenar:", columnas_numericas)
    orden_ascendente = st.radio("Orden:", ["Ascendente", "Descendente"])

    if columna_orden:
        df_ordenado = df.sort_values(by=columna_orden, ascending=(orden_ascendente == "Ascendente"))
        st.write(f"Datos ordenados por {columna_orden} ({orden_ascendente}):")
        st.write(df_ordenado)
    
    # Filtrar los datos por un valor numérico
    columna_filtrar = st.selectbox("Selecciona una columna numérica para filtrar:", columnas_numericas)
    min_value = df[columna_filtrar].min()
    max_value = df[columna_filtrar].max()
    filtro = st.slider(f"Filtra los valores de {columna_filtrar}", min_value, max_value, (min_value, max_value))
    
    df_filtrado = df[df[columna_filtrar].between(filtro[0], filtro[1])]
    st.write(f"Datos filtrados por {columna_filtrar} entre {filtro[0]} y {filtro[1]}:")
    st.write(df_filtrado)

    # Descargar los datos filtrados en CSV
    st.download_button("Descargar los datos filtrados en CSV", df_filtrado.to_csv(index=False), "datos_filtrados.csv", "text/csv")
