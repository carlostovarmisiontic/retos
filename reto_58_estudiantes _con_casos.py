def promedio_superior(p_nota):
    """Calcular el promedio total del grupo, incluyendo unicamente las notas superiores a la nota dada como parametro

    Parámetros:
    -----------
        nota (float):
            Nota minima con la cual se calcula cuantas notas ingresan al promedio.
            
    Retorna:
    --------
        str: "{average} es el promedio total", el promedio debe tener 2 decimales
        -En caso de que el dato dado por parametro no se pueda convertir a float "Error en el dato ingresado"
        -En caso de que ninguna nota supere el valor del parametro 'Ninguna nota supera {p_nota}'
    """
    students = {'a': {'name':'Juan','notas':[3.1,2.2,2.5,3.9,3.2]}, \
        'j': {'name':'Jenny','notas':[2,3.7,2,2,2.2]}, \
        'c': {'name':'Ana','notas':[2.6,2.7,2.1,2.9,2.2]}, \
        'y': {'name':'Pedro','notas':[2,3.5,2,2,2.2]}, \
        'x': {'name':'Pablo','notas':[2,3.3,3.9,3.2,3.2]}, \
        'l': {'name':'Carlos','notas':[3.2,3.8,2.2,2,2.1]}, \
        'v': {'name':'Maria','notas':[2.8,2.7,2.8,2.9,2.8]}, \
        'r': {'name':'Luisa','notas':[2.8,2.7,3.5,2.5,2.9]}, \
        'b': {'name':'Mario','notas':[2.2,3.2,3,4.2,2.2]}, \
        'g': {'name':'Fabio','notas':[2.4,3.2,3.1,3.2,2.2]}}  
    try:
        p_nota = float(p_nota)  
    except:
        return "Error en el dato ingresado"
    students_list = list(students.values())
    quantity = 0
    total = 0
    for student in students_list:
        total_notes = list(filter(lambda note: note > p_nota, student['notas']))
        quantity += len(total_notes)
        total += sum(total_notes)
    try:
        return f'{round(total/quantity, 2)} es el promedio total'
    except:
        return f'Ninguna nota supera {p_nota}'


print(promedio_superior(1))
print(promedio_superior('4'))
print(promedio_superior(5))
print(promedio_superior('hola'))
print(promedio_superior({}))
