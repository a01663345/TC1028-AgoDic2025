"""
Escribe un programa que calcule la longitud del cateto opuesto de un triángulo
rectángulo cuya hipotenusa es dada por el usuario y tiene un ángulo base de 30º

Usa la siguiente fórmula

sin θ = cateto opuesto/hipotenusa
"""

import math

ANGLE = math.radians(30)

print("\t<<----- CATETO OPUESTO----->>")
print("¡Bienvenido!")
print()
h: float = float(input("Por favor, ingresa la hipotenusa:"))
co: float = math.sin(ANGLE) * h

print()
print("==================================================")
print()
print(f"Resultado {co:.2f}")
print()
print("==================================================")
print()
print("\t<<----- ¡Gracias! ----->>")
