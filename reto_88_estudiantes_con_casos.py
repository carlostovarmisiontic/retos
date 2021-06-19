def contar_notas(p_nota):
    """Contar cada una de las notas de los estudiantes, cuando dicha nota este por debajo de una nota dada como parametro

    Parámetros:
    -----------
        nota (float):
            Nota minima con la cual se calcula cuantas notas estan por debajo.

    Retorna:
    --------
        str: "{quantity} notas a cambiar"
        -En caso de que el dato ingresado no se pueda convertir a float "Error en el dato ingresado"
    """
    students = {'a': {'name': 'Juan', 'notas': [3.1, 2.2, 2.5, 3.9, 3.2]}, \
        'j': {'name': 'Jenny', 'notas': [2, 3.7, 2, 2, 2.2]}, \
        'c': {'name': 'Ana', 'notas': [2.6, 2.7, 2.1, 2.9, 2.2]}, \
        'y': {'name': 'Pedro', 'notas': [2, 3.5, 2, 2, 2.2]}, \
        'x': {'name': 'Pablo', 'notas': [2, 3.3, 3.9, 3.2, 3.2]}, \
        'l': {'name': 'Carlos', 'notas': [3.2, 3.8, 2.2, 2, 2.1]}, \
        'v': {'name': 'Maria', 'notas': [2.8, 2.7, 2.8, 2.9, 2.8]}, \
        'r': {'name': 'Luisa', 'notas': [2.8, 2.7, 3.5, 2.5, 2.9]}, \
        'b': {'name': 'Mario', 'notas': [2.2, 3.2, 3, 4.2, 2.2]}, \
        'g': {'name': 'Fabio', 'notas': [2.4, 3.2, 3.1, 3.2, 2.2]}}
    try:
        p_nota = float(p_nota)
    except:
        return "Error en el dato ingresado"
    students_list = list(students.values())
    quantity = 0
    for student in students_list:
        quantity += len(list(filter(lambda note: note < p_nota, student['notas'])))
    return f'{quantity} notas a cambiar'


print(contar_notas(2))
print(contar_notas('hola'))
print(contar_notas('4'))
print(contar_notas(5))
print(contar_notas({}))
