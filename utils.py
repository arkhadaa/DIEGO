import requests
import pandas as pd

def get_data_from_api():
    """
    Conecta con la API REST Countries y devuelve los datos en formato JSON.
    """
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener datos de la API. Código: {response.status_code}")

def preprocess_data(data):
    """
    Procesa los datos JSON obtenidos de la API y los convierte en un DataFrame.
    """
    countries = []
    for country in data:
        countries.append({
            "Nombre": country.get("name", {}).get("common", ""),
            "Región": country.get("region", ""),
            "Población": country.get("population", 0),
            "Área (km²)": country.get("area", 0),
            "Fronteras": len(country.get("borders", [])),
            "Idiomas": len(country.get("languages", {})),
            "Zonas Horarias": len(country.get("timezones", [])),
        })
    return pd.DataFrame(countries)
