"""
Escribe un programa que calcule el tiempo que tarda en caer un objeto desde
cierta altura cuando se deja en reposo y se desprecia la resistencia del aire.

Recuerda que la fórmula para caída libre desde reposo es:
h = (1/2) g * t ^ 2
t = sqrt(2h/g)

Entrada
Un número recibido en un renglón, correspondiente a:
- altura: (número flotante positivo, en metros).

Salida
Un número (flotante) que representa el tiempo de caída en segundos,
formateado con exactamente 2 decimales.

Ejemplo de ejecución:
>>> 20
2.02
"""

import math

GRAVITY: float = 9.81
height: float = float("Altura en m: ")

time = math.sqrt(2 * height / GRAVITY)
print(f"{time:}")
