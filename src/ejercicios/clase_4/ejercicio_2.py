"""
Crea un programa que reciba una calificación de 0 - 10 con dos decimales.
Si los decimales son mayor o igual a 0.60, la calificación debe subir al
entero mayor más cercano.

Si los decimales son menores a 0.60, la calificación debe bajar al entero
menor más cercano.

Entradas:
- La calificación (Un float positivo mayor o igual a 0)

Salidas:
- La calificación final

Ejemplo de ejecución:
>>> 7.68
8
"""

import math

calificacion = float(input("Calificación: "))
trunc_c = math.trunc(calificacion)
# 9.87 - 9 = 0.87
decimales = calificacion - trunc_c
if decimales == 0:
    print(calificacion)
elif decimales >= 0.60:
    print(math.ceil(calificacion))
else:
    print(math.floor(calificacion))
