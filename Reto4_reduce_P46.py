from functools import reduce

def mejor_promedio_anual(datos:dict)->tuple:
    promedio_empleados: list = []
    #Recorre todos los valores del diccionario principal
    for valor in datos.values():
        #Variables temporales para el total de ventas y contador
        total_ventas: int = 0
        cont: int = 0
        #Recorre la lista ventas
        for ventas in valor["ventas"]:
            #Recorre los valores de los diccionarios de la lista
            for articulos in ventas.values():
                #Cuenta 
                cont += len(articulos)
                sumatoria = lambda total=0, venta=0: total+venta
                total_ventas += reduce( sumatoria, articulos.values() )
        # Obtención de la codificación para el código de la tupla
        # conversión del nit a una lista
        cedula = list(valor["cedula"])
        # Obtención de los números pares e impares con la función filter y list comprenhension
        pares = [int(x) for x in list(filter(lambda x: int(x)%2 == 0, cedula))]
        impares = [int(x) for x in list(filter(lambda x: int(x)%2 == 1, cedula))]
        # Con la función reduce se suman los impares y se multiplican con cada número par con la
        # función map
        codificacion = list(map(lambda n: n*(reduce(lambda acum=0, element=0: acum + element, impares)), pares))
        # Con la función map convertimos cada elemento de la lista codificación en cadena de caracteres
        codigo_unico: str = valor["nombre"][:3]+''.join(map(str, codificacion))
        promedio: float = round((total_ventas/cont), 2)
        tupla: tuple = (codigo_unico, valor["nombre"], promedio)
        promedio_empleados.append(tupla)

    return obtener_promedio_mayor(promedio_empleados)

def obtener_promedio_mayor(promedio_ventas: list) -> tuple:
    mayor = 0
    tupla = tuple()
    for codigo, nombre, promedio in promedio_ventas:
        if promedio > mayor:
            mayor = promedio
            tupla = (codigo, nombre, promedio)
    return tupla

"""
# Trabajor del año
datos = {
    "Jo0986": {
        "nombre": 'Jorge Alfredo',
        "cedula": '098654',
        "ventas": [
            {
                "enero": {
                    "bmw": 15000000,
                    "jeep": 12400000,
                    "audi": 98500000,
                    "jaguar": 23300000
                }
            },
            {
                "febrero": {
                    "bmw": 1434000,
                    "jeep": 1200000,
                    "audi": 7000000,
                    "jaguar": 9000000
                }
            },
            {
                "marzo": {
                    "bmw": 13000000,
                    "jeep": 12400000,
                    "audi": 1600000,
                    "jaguar": 1800000
                }
            },
            {
                "abril": {
                    "bmw": 12900000,
                    "jeep": 22450000,
                    "audi": 31400000,
                    "jaguar": 1300000
                }
            },
            {
                "mayo": {
                    "bmw": 21800000,
                    "jeep": 632750000,
                    "audi": 81200000,
                    "jaguar": 7200000
                }
            },
            {
                "junio": {
                    "bmw": 10700000,
                    "jeep": 22000000,
                    "audi": 19300000,
                    "jaguar": 5200000
                }
            },
            {
                "julio": {
                    "bmw": 16200000,
                    "jeep": 27180000,
                    "audi": 15300000,
                    "jaguar": 7040000
                }
            },
            {
                "agosto": {
                    "bmw": 15400000,
                    "jeep": 22050000,
                    "audi": 11900000,
                    "jaguar": 2800000
                }
            },
            {
                "septiembre": {
                    "bmw": 18100000,
                    "jeep": 29540000,
                    "audi": 81200000,
                    "jaguar": 6400000
                }
            },
            {
                "octubre": {
                    "bmw": 61400000,
                    "jeep": 52120000,
                    "audi": 61400000,
                    "jaguar": 7500000
                }
            },
            {
                "noviembre": {
                    "bmw": 41300000,
                    "jeep": 52230000,
                    "audi": 31700000,
                    "jaguar": 4200000
                }
            },
            {
                "diciembre": {
                    "bmw": 41000000,
                    "jeep": 52480000,
                    "audi": 125000000,
                    "jaguar": 1000000
                }
            }
        ]
    },
    "Sm2345": {
        "nombre": 'Smith',
        "cedula": '234513',
        "ventas": [
            {
                "enero": {
                    "bmw": 1980000,
                    "jeep": 24200000,
                    "audi": 3940000,
                    "jaguar": 4500000
                }
            },
            {
                "febrero": {
                    "bmw": 4910000,
                    "jeep": 36400000,
                    "audi": 3140000,
                    "jaguar": 4280000
                }
            },
            {
                "marzo": {
                    "bmw": 1920000,
                    "jeep": 43300000,
                    "audi": 2440000,
                    "jaguar": 4210000
                }
            },
            {
                "abril": {
                    "bmw": 9480000,
                    "jeep": 45200000,
                    "audi": 5640000,
                    "jaguar": 4502000
                }
            },
            {
                "mayo": {
                    "bmw": 9620000,
                    "jeep": 45700000,
                    "audi": 5440000,
                    "jaguar": 9380000
                }
            },
            {
                "junio": {
                    "bmw": 9800000,
                    "jeep": 49600000,
                    "audi": 6750000,
                    "jaguar": 2890000
                }
            },
            {
                "julio": {
                    "bmw": 8590000,
                    "jeep": 46200000,
                    "audi": 1940000,
                    "jaguar": 7520000
                }
            },
            {
                "agosto": {
                    "bmw": 1350000,
                    "jeep": 96200000,
                    "audi": 9640000,
                    "jaguar": 8570000
                }
            },
            {
                "septiembre": {
                    "bmw": 2140000,
                    "jeep": 55400000,
                    "audi": 1380000,
                    "jaguar": 9480000
                }
            },
            {
                "octubre": {
                    "bmw": 2550000,
                    "jeep": 34400000,
                    "audi": 1430000,
                    "jaguar": 4450000
                }
            },
            {
                "noviembre": {
                    "bmw": 4350000,
                    "jeep": 13500000,
                    "audi": 25400000,
                    "jaguar": 4520000
                }
            },
            {
                "diciembre": {
                    "bmw": 5260000,
                    "jeep": 83900000,
                    "audi": 7420000,
                    "jaguar": 3400000
                }
            }
        ]
    }
}

print(mejor_promedio_anual(datos))

#-------------------------CASO PRIVADO-------------------------
datos = {
    "La1133": {
        "nombre": 'Laura Villamil',
        "cedula": '1133234567',
        "ventas": [
            {
                "enero": {
                    "bmw": 24000000,
                    "jeep": 10400000,
                    "audi": 82500000,
                    "jaguar": 23300000
                }
            },
            {
                "febrero": {
                    "bmw": 2434000,
                    "jeep": 1200000,
                    "audi": 7000000,
                    "jaguar": 9000000
                }
            },
            {
                "marzo": {
                    "bmw": 53000000,
                    "jeep": 12400000,
                    "audi": 1600000,
                    "jaguar": 1800000
                }
            },
            {
                "abril": {
                    "bmw": 12900000,
                    "jeep": 22450000,
                    "audi": 31400000,
                    "jaguar": 1300000
                }
            },
            {
                "mayo": {
                    "bmw": 21800000,
                    "jeep": 632750000,
                    "audi": 91200000,
                    "jaguar": 7200000
                }
            },
            {
                "junio": {
                    "bmw": 10700000,
                    "jeep": 22000000,
                    "audi": 19300000,
                    "jaguar": 5200000
                }
            },
            {
                "julio": {
                    "bmw": 16200000,
                    "jeep": 27180000,
                    "audi": 15300000,
                    "jaguar": 7040000
                }
            },
            {
                "agosto": {
                    "bmw": 15400000,
                    "jeep": 22050000,
                    "audi": 11900000,
                    "jaguar": 2800000
                }
            },
            {
                "septiembre": {
                    "bmw": 18100000,
                    "jeep": 29540000,
                    "audi": 81200000,
                    "jaguar": 6400000
                }
            },
            {
                "octubre": {
                    "bmw": 51400000,
                    "jeep": 22120000,
                    "audi": 61400000,
                    "jaguar": 7500000
                }
            },
            {
                "noviembre": {
                    "bmw": 41300000,
                    "jeep": 52230000,
                    "audi": 31700000,
                    "jaguar": 4200000
                }
            },
            {
                "diciembre": {
                    "bmw": 41000000,
                    "jeep": 52480000,
                    "audi": 125000000,
                    "jaguar": 1000000
                }
            }
        ]
    },
    "Sa1155": {
        "nombre": 'Sara',
        "cedula": '1155198234',
        "ventas": [
            {
                "enero": {
                    "bmw": 3980000,
                    "jeep": 24200000,
                    "audi": 3940000,
                    "jaguar": 4500000
                }
            },
            {
                "febrero": {
                    "bmw": 4910000,
                    "jeep": 46400000,
                    "audi": 3140000,
                    "jaguar": 4280000
                }
            },
            {
                "marzo": {
                    "bmw": 1920000,
                    "jeep": 43300000,
                    "audi": 2440000,
                    "jaguar": 4210000
                }
            },
            {
                "abril": {
                    "bmw": 5480000,
                    "jeep": 65200000,
                    "audi": 5640000,
                    "jaguar": 4502000
                }
            },
            {
                "mayo": {
                    "bmw": 9620000,
                    "jeep": 25700000,
                    "audi": 5440000,
                    "jaguar": 9380000
                }
            },
            {
                "junio": {
                    "bmw": 7600000,
                    "jeep": 69600000,
                    "audi": 6750000,
                    "jaguar": 3890000
                }
            },
            {
                "julio": {
                    "bmw": 6590000,
                    "jeep": 46200000,
                    "audi": 1940000,
                    "jaguar": 7520000
                }
            },
            {
                "agosto": {
                    "bmw": 1350000,
                    "jeep": 96200000,
                    "audi": 9640000,
                    "jaguar": 8570000
                }
            },
            {
                "septiembre": {
                    "bmw": 2140000,
                    "jeep": 55400000,
                    "audi": 1380000,
                    "jaguar": 9480000
                }
            },
            {
                "octubre": {
                    "bmw": 4550000,
                    "jeep": 34400000,
                    "audi": 1430000,
                    "jaguar": 4450000
                }
            },
            {
                "noviembre": {
                    "bmw": 4350000,
                    "jeep": 23500000,
                    "audi": 25400000,
                    "jaguar": 4520000
                }
            },
            {
                "diciembre": {
                    "bmw": 2260000,
                    "jeep": 33900000,
                    "audi": 9420000,
                    "jaguar": 2400000
                }
            }
        ]
    }
}

print(mejor_promedio_anual(datos))
"""
