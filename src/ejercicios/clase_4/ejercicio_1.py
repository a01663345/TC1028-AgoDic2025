"""
Crea un programa que pida al usuario dos números enteros y que diga si:
- Son iguales
- Cual es mayor y cual es menor

Ejemplo de ejecución:
>>> 99
>>> 20

90 es mayor que 20

- - - -
>>> 99
>>> 99

Ambos números son iguales
"""

num_a = int(input("Num A:"))
num_b = int(input("Num B:"))

if num_a == num_b:
    print("Ambos números son iguales")
elif num_a > num_b:
    print(f"{num_a} es mayor que {num_b}")
else:
    print(f"{num_a} es menor que {num_b}")
