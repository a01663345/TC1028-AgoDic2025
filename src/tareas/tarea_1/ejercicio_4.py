"""
Odómetro de 5 digitos con rollover

Un odometro de 5 digitos regresa a 00000 cuando supera 99999. Calcula la lectura
después de un viaje.

Entradas:
- La lectura actual del odometro (0-99999)
- La distancia viajada (entero)

Salida:
- La nueva lectura del odómetro


Ejemplo de ejecución:
>>> 99990
>>> 25

Salida
15
"""

MAX_VALUE = 99999 + 1

lectura_actual: int = int(input("Lectura Actual: "))
lectura_actual += int(input("Distancia Viajada: "))

print(lectura_actual % MAX_VALUE)
