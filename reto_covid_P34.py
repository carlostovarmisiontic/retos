
import pandas as pd


def estudio_covid(ruta_datos: str) -> dict:
    if ruta_datos.endswith('.csv'):
        try:
            df = pd.read_csv(ruta_datos)
        except:
            return "Error al obtener los datos"
        # Obtiene el valor que más se repite
        dia_mas_contagios = df["Fecha diagnostico"].mode()
        dia_mas_contagios = dia_mas_contagios[0]
        # Filtra los registros que sean de bogotá
        filtro_dia = df.loc[:,'Fecha diagnostico'] == dia_mas_contagios
        dia_mayor_contagios = df[filtro_dia]
        # Cuenta los registros (numeros de contagios)
        # Número de fallecidos
        filtro_fallecidos = dia_mayor_contagios.loc[:,'atención'] == 'Fallecido'
        fallecidos = dia_mayor_contagios[filtro_fallecidos]

        # Crea el diccionario respuesta
        respuesta: dict = {
            "fecha_mayor_contagio": dia_mas_contagios,
            "cantidad_contagios": dia_mayor_contagios['Fecha diagnostico'].count(),
            "fallecidos": fallecidos['atención'].count()
        }
    else:
        return "Extensión de archivo inválida"
    
    return respuesta


#print(estudio_covid("casos_covid.csv"))

