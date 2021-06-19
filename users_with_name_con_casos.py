import pandas as pd
    
def get_users_with_name(pname:str, url):    
    """Descripción:
    -----------
    Retorna la cantidad de personas cuyo nombre es igual o similar a uno dado por parámetro

    Parámetros:
    -----------
        pname (str):
            Nombre buscado con el cual se espera encontrar coincidencias.
            
    Retorna:
    --------
        int: 0... N        
    """
    try:
        pname = str(pname)
    except:
        pass
    data = pd.read_json(url)
    frame1 = pd.DataFrame([info for info in data['results']])
    data = pd.concat([frame1, pd.DataFrame((name for name in frame1['name'] if pname in name['first'] ))], axis=1)
    try:
        return data.count()['first']        
    except:
        return 0

print(get_users_with_name(1, 'https://magicsolutions.co/users.json'))
print(get_users_with_name('Alan', 'https://magicsolutions.co/users.json'))
print(get_users_with_name('Alban', 'https://magicsolutions.co/users.json'))
print(get_users_with_name([8,5], 'https://magicsolutions.co/users.json'))
print(get_users_with_name('al', 'https://magicsolutions.co/users.json'))