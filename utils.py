import requests
import pandas as pd

def get_data_from_api():
    """
    Conecta con la API REST Countries y devuelve los datos en formato JSON.
    """
    url = "https://restcountries.com/v3.1/all"
    
    try:
        response = requests.get(url, timeout=180)  # Aumentamos el timeout a 180 segundos
        response.raise_for_status()  # Verifica si hay algún error en la solicitud
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return None  # Si hay un error, retornamos None

def preprocess_data(data):
    """
    Procesa los datos JSON obtenidos de la API y los convierte en un DataFrame.
    Extrae los campos necesarios: nombre común, región, población, área, fronteras, idiomas y zonas horarias.
    """
    countries = []
    
    for country in data:
        countries.append({
            "Nombre": country.get("name", {}).get("common", ""),
            "Región": country.get("region", ""),
            "Población": country.get("population", 0),
            "Área (km²)": country.get("area", 0),
            "Fronteras": len(country.get("borders", [])),  # Número de países con frontera
            "Idiomas": len(country.get("languages", {})),  # Número de idiomas oficiales
            "Zonas Horarias": len(country.get("timezones", [])),  # Número de zonas horarias
        })
    
    # Convertimos la lista de diccionarios a un DataFrame de pandas
    df = pd.DataFrame(countries)
    return df  # Retorna el DataFrame
