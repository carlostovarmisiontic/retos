def crear_codigo_mascotas (mascotas: list):
    for mascota in mascotas:
        mascota['edad'] = str(mascota['edad']) if mascota['edad'] > 10 else '0'+str(mascota['edad'])
   
    especie = [mascota['especie'][0:2].upper() for mascota in mascotas]
    nombre = [mascota['nombre'][0:2].upper() for mascota in mascotas]
    edad =  [mascota['edad'] for mascota in mascotas]
    prop = [mascota['propietario'][0:2].upper() for mascota in mascotas]
    
    codigos = [es+no+ed+pp for es,no,ed,pp in (list(zip(especie,nombre,edad,prop)))]
    codigos = cambiar_repetidos(codigos) if len(codigos) != len(set(codigos)) else codigos
    salida = [(mascotas[idx]['id_mascota'],codigos[idx]) for idx in range(len(codigos))]
    return salida
    
def cambiar_repetidos(codigos:list):
    salida = []
    for cod in codigos:
        try:
            idx = salida.index(cod)
        except:
            idx = -1
        if idx != -1:
            cont = len(list(filter(lambda x: x.startswith(cod),salida)))
            salida.append(cod+str(cont))
        else:
            salida.append(cod)
    return salida

## Casos de pruebas

'''
mascotas = [
    dict(id_mascota='MASC_001',nombre='Tigger',edad=5,
         especie='Felino',raza='Angora',propietario='Yina'),
    dict(id_mascota='MASC_002',nombre='Simona',edad=8,
         especie='Canino',raza='Dalmata',propietario='Paula'),
    dict(id_mascota='MASC_003',nombre='Timina',edad=5,
         especie='Felino',raza='Angora',propietario='Yina')
]
print(crear_codigo_mascotas(mascotas))

mascotas2 = [
    dict(id_mascota='MASC_001',nombre='Lucas',edad=5,
         especie='Canino',raza='Pekines',propietario='Alejandro'),
    dict(id_mascota='MASC_002',nombre='Tita',edad=13,
         especie='Canino',raza='Puddle',propietario='Paula'),
    dict(id_mascota='MASC_003',nombre='Nieves',edad=10,
         especie='Felino',raza='Criolla',propietario='Maria')
]
print(crear_codigo_mascotas(mascotas2))

mascotas3 = [
    dict(id_mascota='MASC_001',nombre='Tigger',edad=4,
         especie='Felino',raza='Criollo',propietario='Alejandro'),
    dict(id_mascota='MASC_002',nombre='Ammy',edad=10,
         especie='Felino',raza='Criollo',propietario='Alejandro'),
    dict(id_mascota='MASC_003',nombre='Luci',edad=1,
         especie='Felino',raza='Criollo',propietario='Alejandro')
]
print(crear_codigo_mascotas(mascotas3))

mascotas4 = [
    dict(id_mascota='MASC_001',nombre='Tita',edad=8,
         especie='Felino',raza='Criollo',propietario='Catalina'),
    dict(id_mascota='MASC_002',nombre='Timoteo',edad=8,
         especie='Felino',raza='Criollo',propietario='Carmen'),
    dict(id_mascota='MASC_003',nombre='Titina',edad=8,
         especie='Felino',raza='Criollo',propietario='Carlos')
]
print(crear_codigo_mascotas(mascotas4))
'''