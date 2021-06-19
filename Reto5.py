# from matplotlib import pyplot as plt
import pandas as pd

def evaluar_csv(ruta_archivo:str):
    if ruta_archivo.endswith('.csv'):
        try:
            dt_analizar = pd.read_csv(ruta_archivo,delimiter=';',
                               encoding='UTF-8', na_values=['?'])
            #print(data)
        except:
            return 'Ocurrio un error al leer el archivo. Valide la ruta'
        try:
            data = {'ANIO': dt_analizar['ANIO'],'SEXO': dt_analizar['SEXO'],'EDAD': dt_analizar['EDAD'], 'TIPO_LESION': dt_analizar['TIPO_LESION']}
            dt = pd.DataFrame(data)
            dt_respuesta = dt.value_counts()
            #dt_respuesta = dt_respuesta.unstack()
            #dt_respuesta.plot(kind='bar')
            #dt_respuesta.to_csv('respuesta.csv')
            #plt.show()
            return dt_respuesta.to_dict()
        except Exception as exp:
            print('As ocurred error ',str(exp))
    else:
        return 'Extensión inválida.'


csv = 'https://raw.githubusercontent.com/Alejowilches0112/retos_mintic/master/Superservicios-Informacion_de_Accidentes_de_Origen_El_ctrico-Formato19.csv'
print(evaluar_csv(csv))
