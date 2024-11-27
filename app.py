import streamlit as st
from utils import get_data_from_api, preprocess_data
import introduccion
import interaccion
import visualizaciones

# Cargar los datos desde la API y preprocesarlos
try:
    data = get_data_from_api()  # Llamamos a la función que obtiene los datos de la API
    if data:
        df = preprocess_data(data)  # Procesamos los datos para extraer la información necesaria
        st.success("Datos cargados exitosamente.")
    else:
        st.error("No se pudieron cargar los datos. Intenta nuevamente.")
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")

# Página de Interacción con los Datos
page = st.sidebar.radio("Selecciona la página", ["App", "Introducción", "Interacción con los Datos", "Gráficos Interactivos"])

if page == "App":
    st.write("Contenido de la App")
elif page == "Introducción":
    introduccion.app()
elif page == "Interacción con los Datos":
    if 'df' in locals():
        interaccion.app(df)  # Pasamos df como argumento aquí
    else:
        st.error("Los datos no se han cargado correctamente.")
elif page == "Gráficos Interactivos":
    if 'df' in locals():
        visualizaciones.app(df)  # Pasamos df como argumento aquí
    else:
        st.error("Los datos no se han cargado correctamente.")
