import streamlit as st
from utils import get_data_from_excel
import introduccion
import interaccion
import visualizaciones

# aqui cargamos los datos desde el archivo Excel
try:
    df = get_data_from_excel()  
    if df is not None:
        st.success("Datos cargados exitosamente desde el archivo Excel.")
    else:
        st.error("No se pudieron cargar los datos. Asegúrate de que el archivo Excel exista.")
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")

# Pagina de Interacción con los datos
page = st.sidebar.radio("Selecciona la página", ["App", "Introducción", "Interacción con los Datos", "Gráficos Interactivos"])

if page == "App":
    st.write("Contenido de la App")
elif page == "Introducción":
    introduccion.app()
elif page == "Interacción con los Datos":
    if df is not None:
        interaccion.app(df)  # Pasamos df como argumento aqui
    else:
        st.error("Los datos no se han cargado correctamente.")
elif page == "Gráficos Interactivos":
    if df is not None:
        visualizaciones.app(df)  # Pasamos df como argumento aquí
    else:
        st.error("Los datos no se han cargado correctamente.")
