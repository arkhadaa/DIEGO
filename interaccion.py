import streamlit as st
import io
from utils import preprocess_data, get_data_from_api

# Función para permitir la descarga de datos filtrados
def download_data(df):
    # Convertir el DataFrame a CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()

    # Botón para descargar el CSV
    st.download_button(
        label="Descargar datos filtrados en CSV",
        data=csv_data,
        file_name="datos_filtrados.csv",
        mime="text/csv",
    )

# Página de Interacción con los Datos
def app(df):  # Aceptamos df como argumento
    st.title("Interacción con los Datos")
    
    # Mostrar los datos originales
    st.header("Mostrar Datos Originales")
    st.write("A continuación se muestran los datos originales obtenidos de la API.")
    st.dataframe(df)

    # Análisis de estadísticas básicas
    st.header("Análisis Básico de los Datos")
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()  # Solo columnas numéricas
    columna_seleccionada = st.selectbox("Selecciona una columna para analizar:", columnas_numericas)

    if columna_seleccionada:
        st.subheader(f"Estadísticas para {columna_seleccionada}:")
        media = df[columna_seleccionada].mean()
        mediana = df[columna_seleccionada].median()
        desviacion_estandar = df[columna_seleccionada].std()

        # Mostrar las estadísticas
        st.write(f"**Media**: {media:,.2f}")
        st.write(f"**Mediana**: {mediana:,.2f}")
        st.write(f"**Desviación Estándar**: {desviacion_estandar:,.2f}")

    # Ordenar los datos
    st.header("Ordenar los Datos")
    columna_orden = st.selectbox("Selecciona una columna para ordenar:", columnas_numericas)
    orden_ascendente = st.radio("Orden:", ["Ascendente", "Descendente"])

    if columna_orden:
        df_ordenado = df.sort_values(by=columna_orden, ascending=(orden_ascendente == "Ascendente"))
        st.write(f"Datos ordenados por {columna_orden} ({orden_ascendente}):")
        st.dataframe(df_ordenado)

    # Filtrar los datos por rango
    st.header("Filtrar Datos por Rangos")
    columna_filtro = st.selectbox("Selecciona una columna para filtrar:", columnas_numericas)

    if columna_filtro:
        min_valor, max_valor = int(df[columna_filtro].min()), int(df[columna_filtro].max())
        rango_seleccionado = st.slider(
            f"Selecciona el rango para {columna_filtro}:",
            min_value=min_valor,
            max_value=max_valor,
            value=(min_valor, max_valor),
        )

        # Filtrar el DataFrame
        df_filtrado = df[(df[columna_filtro] >= rango_seleccionado[0]) & (df[columna_filtro] <= rango_seleccionado[1])]
        st.write(f"Datos filtrados por {columna_filtro} entre {rango_seleccionado[0]} y {rango_seleccionado[1]}:")
        st.dataframe(df_filtrado)

        # Llamar a la función de descarga si el DataFrame filtrado no está vacío
        if not df_filtrado.empty:
            download_data(df_filtrado)  # Permite descargar los datos filtrados
        else:
            st.write("No se encontraron datos para el filtro seleccionado.")
