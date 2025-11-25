"""
Enunciado:
Implementa una función 'convert_kg_to_lb' que reciba como parámetro un valor
numérico llamado 'kg' que corresponde al valor que se desea convertir de 
kilogramos a libras.

El valor introducido no puede ser menor o igual que '0', si se introduce un
valor menor o igual a '0' se debe crear un ValueError. El valor introducido
debe ser de type numérico de manera que si se introduce otro valor que no sea
numérico se deberá crear un TypeError.

Parámetros:
kg = Valor numérico que representa a los kilogramos para convertir a libras.

Ejemplo:
    Entrada: 50
    Salida: 110.23

    Entrada: 0
    Salida: ValueError

    Entrada: 'abc'
    Salida: TypeError
"""


def kg_to_lb(kg):
    try:        
        if kg>0: 
            return round(kg*2.20462,2)
        else: 
            raise ValueError("El valor tiene que ser mayor a 0")
    except TypeError:
        raise ("El valor tiene que ser de tipo numérico")

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script

print(kg_to_lb(50))
