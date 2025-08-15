"""
Crea un programa que pregunte al usuario su edad y el año actual, como resultado 
le indicará el año en que cumplirá 100 años.
Ignora el mes y día de nacimiento, solo nos interesa el año en el que el usuario
nació.

Salida:
El año de los 100 años.
"""

age = int(input())
current_year = int(input())

result = (current_year - age) + 100
print(f"Cumplirás 100 anios en {result}")
