import pandas as pd

def get_data_from_excel():
    """
    Carga los datos desde un archivo Excel local.
    """
    try:
        # Aca el archivo Excel lo lee y devuelve un DataFrame
        df = pd.read_excel('datos_paises_procesados.xlsx')
        return df
    except Exception as e:
        print(f"Error al cargar los datos desde el archivo Excel: {e}")
        return None

def preprocess_data(data):
    """
    Procesa los datos cargados y realiza cualquier transformación necesaria.
    (Esta función puede no ser necesaria si los datos ya están procesados en Excel).
    """
    return data  # Si no se necesita procesamiento, simplemente retorna los datos
