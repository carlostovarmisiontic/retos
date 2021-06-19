import pandas as pd

def get_older_users(age, url):
    """Descripción:
    -----------
    Retorna la cantidad de personas cuya edad es mayor a una dada por parámetro

    Parámetros:
    -----------
        age (int):
            Edad mínima con la cual se buscan y se cuentan las personas.
            
    Retorna:
    ----------        
        int: 0... N        
            Cantidad de usuarios con una edad mayor a la dada por parámetro

    Except:
    ----------
        int: 0
            En caso de que no se pueda convertir el parámetro a int
    """
    try:
        age = int(age)
    except:
        return 0
    data = pd.read_json(url)
    frame1 = pd.DataFrame([info for info in data['results']])
    data = pd.concat([frame1, pd.DataFrame((dob for dob in frame1['dob'] if dob['age'] > age))], axis=1)
    return data.count()['age']


print(get_older_users(42,'https://magicsolutions.co/users.json'))
print(get_older_users('32','https://magicsolutions.co/users.json'))
print(get_older_users('a','https://magicsolutions.co/users.json'))
print(get_older_users({},'https://magicsolutions.co/users.json'))
print(get_older_users([],'https://magicsolutions.co/users.json'))