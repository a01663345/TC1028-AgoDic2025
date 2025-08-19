"""
Escribe un programa que calcule la temperatura de un objeto después de un cierto
tiempo usando la ley de enfriamiento de Newton:

T(t) = Tamb + (T0 - Tamb) * e-kt

Entrada
Cuatro números, uno por renglón, correspondientes a:
T0 = Temperatura Inicial
Tamb = Temperatura ambiente
k = Constante de enfriamiento (float positivo)
t = Tiempo transcurrido (float positivo en minutos)

Salida
Un número (flotante) con la temperatura T(t) en °C,
formateado con exactamente 2 decimales.

Ejemplo de ejecución:
>>> 90
>>> 25
>>> 0.1
>>> 10
48.91
"""

import math

t0 = float(input("T0: "))
t_amb = float(input("T Amb: "))
k = float(input("K: "))
t = float(input("t: "))

res = t_amb + (t0 - t_amb) * math.pow(math.e, -(k * t))
print(f"{res: .2f}")
