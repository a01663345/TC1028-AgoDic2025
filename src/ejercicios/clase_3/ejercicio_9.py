"""
Area de triangulo
"""

import math

a = float(input("Escribe el valor de a: "))
b = float(input("Escribe el valor de b: "))
c = float(input("Escribe el valor de c: "))

s = (a + b + c) / 2
res = s * (s - a) * (s - b) * (s - c)
area = math.sqrt(res)
print(area)
