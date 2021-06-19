from functools import reduce

def mejor_promedio_anual(datos: dict) -> tuple:
    promedio_transacciones: list = []
    for clave, valor in datos.items():
        total_transacciones: int = 0
        cont: int = 0
        for transacciones in valor["ventas"]:
            for mes, sedes in transacciones.items():
                for sede, ventas in sedes.items():
                    total_transacciones += ventas
                    cont += 1
        
        # Obtención de la codificación para el código de la tupla
        # conversión del nit a una lista
        nit = list(valor["nit"])
        # Obtención de los números pares e impares con la función filter y list comprenhension
        pares = [int(x) for x in list(filter(lambda x: int(x)%2 == 0, nit))]
        impares = [int(x) for x in list(filter(lambda x: int(x)%2 == 1, nit))]
        # Con la función "reduce" se suman los impares y se multiplican con cada número par con la
        # función map
        codificacion = list(map(lambda n: n*(reduce(lambda acum=0, element=0: acum + element, impares)), pares))
        # Con la función map convertimos cada elemento de la lista codificación en cadena de caracteres
        cod_nit = ''.join(map(str, codificacion))
        
        codigo = valor["empresa"][0:3] + cod_nit
        promedio = lambda totalventas, cont: total_transacciones / cont
        tupla: tuple = (codigo, valor["empresa"], promedio(total_transacciones, cont))
        promedio_transacciones.append(tupla)

    return obtener_promedio_mayor(promedio_transacciones)

def obtener_promedio_mayor(promedio_transacciones: list) -> tuple:
    mayor = 0
    tupla = tuple()
    for nit, empresa, promedio in promedio_transacciones:
        if promedio > mayor:
            mayor = promedio
            tupla = (nit, empresa, round(promedio,2))
    return tupla

#Caso de prueba 1
datos = {
    "01": {
        "empresa": "Avon",
        "nit": "12345678",
        "url": "www.avon.com.co",
        "ventas": [
            {
                "enero": {
                    "blusas": 250000,
                    "perfumes": 40000,
                    "jeans": 560000,
                    "maquillaje": 280000
                }
            },
            {
                "febrero": {
                    "blusas": 750000,
                    "perfumes": 890000,
                    "jeans": 920000,
                    "maquillaje": 340000
                }
            },
            {
                "marzo": {
                    "blusas": 730000,
                    "perfumes": 460000,
                    "jeans": 820000,
                    "maquillaje": 120000
                }
            },
            {
                "abril": {
                    "blusas": 450000,
                    "perfumes": 640000,
                    "jeans": 920000,
                    "maquillaje": 190000
                }
            },
            {
                "mayo": {
                    "blusas": 580000,
                    "perfumes": 940000,
                    "jeans": 250000,
                    "maquillaje": 630000
                }
            },
            {
                "junio": {
                    "blusas": 940000,
                    "perfumes": 120000,
                    "jeans": 750000,
                    "maquillaje": 340000
                }
            },
            {
                "julio": {
                    "blusas": 120000,
                    "perfumes": 850000,
                    "jeans": 960000,
                    "maquillaje": 540000
                }
            },
            {
                "agosto": {
                    "blusas": 650000,
                    "perfumes": 250000,
                    "jeans": 250000,
                    "maquillaje": 860000
                }
            },
            {
                "septiembre": {
                    "blusass": 640000,
                    "perfumes": 450000,
                    "jeans": 250000,
                    "maquillaje": 940000
                }
            },
            {
                "octubre": {
                    "blusass": 340000,
                    "perfumes": 950000,
                    "jeans": 870000,
                    "maquillaje": 820000
                }
            },
            {
                "noviembre": {
                    "blusas": 830000,
                    "perfumes": 670000,
                    "jeans": 730000,
                    "maquillaje": 820000
                }
            },
            {
                "diciembre": {
                    "blusas": 240000,
                    "perfumes": 340000,
                    "jeans": 150000,
                    "maquillaje": 480000
                }
            }
        ]
    },
    "02": {
        "empresa": "Natura",
        "nit": "7865432",
        "url": "www.natura.com",
        "ventas": [
            {
                "enero": {
                    "blusas": 150000,
                    "perfumes": 920000,
                    "jeans": 280000,
                    "maquillaje": 470000
                }
            },
            {
                "febrero": {
                    "blusas": 750000,
                    "perfumes": 650000,
                    "jeans": 920000,
                    "maquillaje": 570000
                }
            },
            {
                "marzo": {
                    "blusas": 250000,
                    "perfumes": 250000,
                    "jeans": 270000,
                    "maquillaje": 650000
                }
            },
            {
                "abril": {
                    "blusas": 920000,
                    "perfumes": 230000,
                    "jeans": 850000,
                    "maquillaje": 490000
                }
            },
            {
                "mayo": {
                    "blusas": 950000,
                    "perfumes": 830000,
                    "jeans": 190000,
                    "maquillaje": 950000
                }
            },
            {
                "junio": {
                    "blusas": 950000,
                    "perfumes": 950000,
                    "jeans": 530000,
                    "maquillaje": 760000
                }
            },
            {
                "julio": {
                    "blusas": 870000,
                    "perfumes": 960000,
                    "jeans": 480000,
                    "maquillaje": 290000
                }
            },
            {
                "agosto": {
                    "blusas": 780000,
                    "perfumes": 340000,
                    "jeans": 840000,
                    "maquillaje": 340000
                }
            },
            {
                "septiembre": {
                    "blusas": 560000,
                    "perfumes": 840000,
                    "jeans": 850000,
                    "maquillaje": 530000
                }
            },
            {
                "octubre": {
                    "blusas": 190000,
                    "perfumes": 820000,
                    "jeans": 490000,
                    "maquillaje": 820000
                }
            },
            {
                "noviembre": {
                    "blusas": 560000,
                    "perfumes": 670000,
                    "jeans": 450000,
                    "maquillaje": 670000
                }
            },
            {
                "diciembre": {
                    "blusas": 920000,
                    "perfumes": 820000,
                    "jeans": 760000,
                    "maquillaje": 890000
                }
            }
        ]
    }
}
print(mejor_promedio_anual(datos))

#------------------------------------------------------
#Caso de prueba 2
datos = {
    "01": {
        "empresa": "Avon",
        "nit": "12345678",
        "url": "www.avon.com.co",
        "ventas": [
            {
                "enero": {
                    "blusas": 250000,
                    "perfumes": 40000,
                    "jeans": 860000,
                    "maquillaje": 280000
                }
            },
            {
                "febrero": {
                    "blusas": 750000,
                    "perfumes": 890000,
                    "jeans": 920000,
                    "maquillaje": 340000
                }
            },
            {
                "marzo": {
                    "blusas": 730000,
                    "perfumes": 460000,
                    "jeans": 820000,
                    "maquillaje": 120000
                }
            },
            {
                "abril": {
                    "blusas": 450000,
                    "perfumes": 640000,
                    "jeans": 950000,
                    "maquillaje": 190000
                }
            },
            {
                "mayo": {
                    "blusas": 580000,
                    "perfumes": 940000,
                    "jeans": 250000,
                    "maquillaje": 630000
                }
            },
            {
                "junio": {
                    "blusas": 940000,
                    "perfumes": 120000,
                    "jeans": 750000,
                    "maquillaje": 340000
                }
            },
            {
                "julio": {
                    "blusas": 120000,
                    "perfumes": 850000,
                    "jeans": 960000,
                    "maquillaje": 540000
                }
            },
            {
                "agosto": {
                    "blusas": 650000,
                    "perfumes": 550000,
                    "jeans": 250000,
                    "maquillaje": 860000
                }
            },
            {
                "septiembre": {
                    "blusass": 640000,
                    "perfumes": 890000,
                    "jeans": 250000,
                    "maquillaje": 940000
                }
            },
            {
                "octubre": {
                    "blusass": 340000,
                    "perfumes": 950000,
                    "jeans": 570000,
                    "maquillaje": 820000
                }
            },
            {
                "noviembre": {
                    "blusas": 990000,
                    "perfumes": 670000,
                    "jeans": 730000,
                    "maquillaje": 820000
                }
            },
            {
                "diciembre": {
                    "blusas": 240000,
                    "perfumes": 340000,
                    "jeans": 150000,
                    "maquillaje": 580000
                }
            }
        ]
    },
    "02": {
        "empresa": "Yanbal",
        "nit": "7865432",
        "url": "www.yanbal.com",
        "ventas": [
            {
                "enero": {
                    "blusas": 280000,
                    "perfumes": 920000,
                    "jeans": 280000,
                    "maquillaje": 470000
                }
            },
            {
                "febrero": {
                    "blusas": 750000,
                    "perfumes": 970000,
                    "jeans": 920000,
                    "maquillaje": 570000
                }
            },
            {
                "marzo": {
                    "blusas": 250000,
                    "perfumes": 250000,
                    "jeans": 270000,
                    "maquillaje": 650000
                }
            },
            {
                "abril": {
                    "blusas": 920000,
                    "perfumes": 540000,
                    "jeans": 850000,
                    "maquillaje": 490000
                }
            },
            {
                "mayo": {
                    "blusas": 950000,
                    "perfumes": 830000,
                    "jeans": 190000,
                    "maquillaje": 780000
                }
            },
            {
                "junio": {
                    "blusas": 950000,
                    "perfumes": 950000,
                    "jeans": 530000,
                    "maquillaje": 760000
                }
            },
            {
                "julio": {
                    "blusas": 870000,
                    "perfumes": 960000,
                    "jeans": 480000,
                    "maquillaje": 290000
                }
            },
            {
                "agosto": {
                    "blusas": 780000,
                    "perfumes": 340000,
                    "jeans": 840000,
                    "maquillaje": 340000
                }
            },
            {
                "septiembre": {
                    "blusas": 560000,
                    "perfumes": 840000,
                    "jeans": 850000,
                    "maquillaje": 530000
                }
            },
            {
                "octubre": {
                    "blusas": 190000,
                    "perfumes": 820000,
                    "jeans": 870000,
                    "maquillaje": 820000
                }
            },
            {
                "noviembre": {
                    "blusas": 560000,
                    "perfumes": 670000,
                    "jeans": 450000,
                    "maquillaje": 670000
                }
            },
            {
                "diciembre": {
                    "blusas": 920000,
                    "perfumes": 650000,
                    "jeans": 760000,
                    "maquillaje": 890000
                }
            }
        ]
    }
}
print(mejor_promedio_anual(datos))