"""
Escribe un programa que reciba el ancho y largo de un rectángulo y calcule la
medida de la diagonal. Utiliza la función de la biblioteca math correspondiente.

Entrada
Dos números flotantes, uno en cada renglón, correspondientes al ancho y largo
del rectángulo.

Salida
Un número, resultado del cálculo de la diagonal de dicho rectángulo

Ejemplo de ejecución:
>>> 4
>>> 3

5.0
"""

import math

side_a = float(input("Lado A: "))
side_b = float(input("Lado B: "))

res = math.sqrt(side_a**2 + side_b**2)
print(res)

res = math.hypot(side_a, side_b)
print(res)
