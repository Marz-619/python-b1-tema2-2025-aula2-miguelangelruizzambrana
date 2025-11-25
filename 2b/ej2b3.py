"""
Enunciado:
Implementa una función 'triangle_area_calculate', que recibe dos parámetros,
que corresponden a la altura y la base de un triángulo que deben
ser números positivos. Dichos parámetros deben ser nombrados correctamente,
considerando las buenas prácticas de programación PEP8.
La función debe retornar el cálculo del área de un triángulo mediante los
datos introducidos, adicionalmente, el código debe tener comentarios de manera
que se vaya explicando el procedimiento.

Parámetros:
Son dos parámetros, que corresponden a la altura y la base de
un triángulo y deben ser números positivos. Se deben crear correctamente
utilizando las buenas prácticas de programación PEP8.


Ejemplo:
    Entrada:
    triangle_area_calculate(33, 45)

    Salida:
    742.5
"""


def triangle_area_calculate(
    base, height):
    if (base>0 and height>0): #Verificamos que sean positivos
        return ((base*height)/2)
    else: #Algún input es negativo
        raise ValueError("Error, los inputs tienen que ser positivos")


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta
# el script

print(triangle_area_calculate(33,45))
