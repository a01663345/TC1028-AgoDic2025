"""
Problema a resolver
Se requiere calcular la longitud de un cateto de un triángulo rectángulo utilizando el teorema de Pitágoras.

El usuario debe ingresar la longitud de la hipotenusa y del cateto conocido.

El programa calculará el valor del cateto restante.

Usa la fórnuma:
cateto_faltante = sqrt(hypot ^ 2 - cateto_conocido ^ 2)
"""

import math

hipotenusa: float = float(input("Hipotenusa: "))
cateto_conocido: float = float(input("Cateto Conocido: "))

print(math.sqrt(hipotenusa**2 - cateto_conocido**2))
