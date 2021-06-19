
import pandas as pd


def estudio_covid(ruta_datos: str) -> dict:
    if ruta_datos.endswith('.csv'):
        try:
            df = pd.read_csv(ruta_datos)
        except:
            return "Error al obtener los datos"
        # Obtiene el valor que más se repite
        ciudad_mas_contagios = df["Ciudad de ubicación"].mode()
        ciudad_mas_contagios = ciudad_mas_contagios[0]
        # Filtra los registros que sean de bogotá
        filtro_bogota = df.loc[:,'Ciudad de ubicación'] == ciudad_mas_contagios
        contagios_bogota = df[filtro_bogota]
        # Cuenta los registros (numeros de contagios)
        # Número de fallecidos
        filtro_fallecidos_bogota = contagios_bogota.loc[:,
                                                        'atención'] == 'Fallecido'
        fallecidos = contagios_bogota[filtro_fallecidos_bogota]

        # Crea el diccionario respuesta
        respuesta: dict = {
            "ciudad_mayor_contagio": ciudad_mas_contagios,
            "cantidad_contagios": contagios_bogota['Ciudad de ubicación'].count(),
            "fallecidos": fallecidos['atención'].count()
        }
    else:
        return "Extensión de archivo inválida"
    
    return respuesta


#print(estudio_covid("casos_covid.csv"))

