import streamlit as st


# Página de Introducción
def app():
    st.title("Introducción")
    st.write("Este proyecto utiliza la API REST Countries para consultar información detallada sobre países de todo el mundo.")
    
    st.write("La API REST Countries proporciona datos como:")
    st.write("- Nombre del país")
    st.write("- Región geográfica")
    st.write("- Población total")
    st.write("- Área en kilómetros cuadrados")
    st.write("- Número de países con frontera")
    st.write("- Número de idiomas oficiales")
    st.write("- Número de zonas horarias")

    st.markdown(
        "Más información sobre la API REST Countries: [REST Countries API](https://restcountries.com/v3.1/all)"
    )

    st.image("https://restcountries.com/img/logo.png", caption="Logo de REST Countries API", width=300)

app()
