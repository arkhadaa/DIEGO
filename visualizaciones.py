import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import io

# Esta es la Funcion para permitir la descarga de datos filtrados
def download_data(df):
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()
    st.download_button(
        label="Descargar datos filtrados en CSV",
        data=csv_data,
        file_name="datos_filtrados.csv",
        mime="text/csv",
    )

# Aca permitimos la descarga del gráfico como PNG
def download_graph(fig):
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    st.download_button(
        label="Descargar gráfico como PNG",
        data=img_buffer,
        file_name="grafico.png",
        mime="image/png",
    )

def app(df):  # Aseguramos que df se pasa correctamente
    st.title("Visualización de Datos")

    # Validamos si el DataFrame tiene datos
    if df.empty:
        st.error("El DataFrame está vacío. Verifica los datos en el archivo Excel.")
        return

    # Opcion para seleccionar el tipo de gráfico
    tipo_grafico = st.selectbox("Selecciona el tipo de gráfico:", ["Barra", "Dispersión", "Línea", "Histograma", "Pastel"])

    # Seleccion de Variables: Ejes X e Y
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if not columnas_numericas:
        st.error("No se encontraron columnas numéricas en los datos.")
        return

    columna_x = st.selectbox("Selecciona la columna para el eje X", columnas_numericas)
    columna_y = st.selectbox("Selecciona la columna para el eje Y (si aplica)", columnas_numericas)

    # Rango Personalizado para Ejes
    if columna_x:
        min_x, max_x = df[columna_x].min(), df[columna_x].max()
        rango_x = st.slider(f"Selecciona el rango para el eje X ({columna_x})", min_x, max_x, (min_x, max_x))

    if columna_y:
        min_y, max_y = df[columna_y].min(), df[columna_y].max()
        rango_y = st.slider(f"Selecciona el rango para el eje Y ({columna_y})", min_y, max_y, (min_y, max_y))

    # Filtrar los datos segun el rango seleccionado
    df_filtrado = df[(df[columna_x] >= rango_x[0]) & (df[columna_x] <= rango_x[1])]
    if columna_y:
        df_filtrado = df_filtrado[(df_filtrado[columna_y] >= rango_y[0]) & (df_filtrado[columna_y] <= rango_y[1])]

    st.write("Datos filtrados por el rango seleccionado:")
    st.dataframe(df_filtrado)

    # Grafico según la selección
    fig, ax = plt.subplots(figsize=(10, 6))

    if tipo_grafico == "Barra":
        df_filtrado[columna_x].value_counts().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
        ax.set_title(f"Gráfico de Barras: {columna_x}")
        ax.set_xlabel(columna_x)
        ax.set_ylabel('Frecuencia')
    elif tipo_grafico == "Dispersión":
        ax.scatter(df_filtrado[columna_x], df_filtrado[columna_y], color='green')
        ax.set_title(f"Gráfico de Dispersión: {columna_x} vs {columna_y}")
        ax.set_xlabel(columna_x)
        ax.set_ylabel(columna_y)
    elif tipo_grafico == "Línea":
        ax.plot(df_filtrado[columna_x], df_filtrado[columna_y], marker='o', color='orange')
        ax.set_title(f"Gráfico de Línea: {columna_x} vs {columna_y}")
        ax.set_xlabel(columna_x)
        ax.set_ylabel(columna_y)
    elif tipo_grafico == "Histograma":
        ax.hist(df_filtrado[columna_x], bins=30, color='skyblue', edgecolor='black')
        ax.set_title(f"Histograma de {columna_x}")
        ax.set_xlabel(columna_x)
        ax.set_ylabel('Frecuencia')

    st.pyplot(fig)

    # Descargar datos y gráficos
    download_data(df_filtrado)
    download_graph(fig)
