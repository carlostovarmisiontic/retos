
import pandas as pd


def estudio_covid(ruta_datos: str) -> dict:
    if ruta_datos.endswith('.csv'):
        try:
            df = pd.read_csv(ruta_datos)
        except:
            return "Error al obtener los datos"
        # Obtiene el valor que más se repite
        edad_mas_contagios = df["Edad"].mode()
        edad_mas_contagios = edad_mas_contagios[0]
        # Filtra los registros que sean de bogotá
        filtro_edad = df.loc[:,'Edad'] == edad_mas_contagios
        edad__mayor_contagios = df[filtro_edad]
        # Cuenta los registros (numeros de contagios)
        # Número de fallecidos
        filtro_fallecidos = edad__mayor_contagios.loc[:,'atención'] == 'Fallecido'
        fallecidos = edad__mayor_contagios[filtro_fallecidos]

        # Crea el diccionario respuesta
        respuesta: dict = {
            "edad_mayor_contagio": edad_mas_contagios,
            "cantidad_contagios": edad__mayor_contagios['Edad'].count(),
            "fallecidos": fallecidos['atención'].count()
        }
    else:
        return "Extensión de archivo inválida"
    
    return respuesta


#print(estudio_covid("casos_covid.csv"))

