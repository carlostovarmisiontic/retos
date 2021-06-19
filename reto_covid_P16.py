
import pandas as pd


def estudio_covid(ruta_datos: str) -> dict:
    if ruta_datos.endswith('.csv'):
        try:
            df = pd.read_csv(ruta_datos)
        except:
            return "Error al obtener los datos"
        # Obtiene el valor que más se repite
        sexo_mas_contagios = df["Sexo"].mode()
        sexo_mas_contagios = sexo_mas_contagios[0]
        # Filtra los registros con el valor que más se repite
        filtro_contagios = df.loc[:,'Sexo'] == sexo_mas_contagios
        contagios = df[filtro_contagios]
        # Cuenta los registros (numeros de contagios)
        # Número de fallecidos
        filtro_fallecidos = contagios.loc[:,'atención'] == 'Fallecido'
        fallecidos = contagios[filtro_fallecidos]

        # Crea el diccionario respuesta
        respuesta: dict = {
            "sexo_mayor_contagio": sexo_mas_contagios,
            "cantidad_contagios": contagios['Sexo'].count(),
            "fallecidos": fallecidos['atención'].count()
        }
    else:
        return "Extensión de archivo inválida"
    
    return respuesta


#print(estudio_covid("casos_covid.csv"))

