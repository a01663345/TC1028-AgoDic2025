"""
En una universidad cada estudiante cursa 4 materias en el semestre. 
Desarrolla un programa que reciba la calificación de cada materia, calcula el 
promedio de las 4 materias y lo despliega.

Entradas
4 números enteros que representan las calificaciones de 4 materias, un número 
en cada renglón.

Salidas
Un número decimal correspondiente al promedio. Solo con 1 decimales.
"""

c_1 = int(input())
c_2 = int(input())
c_3 = int(input())
c_4 = int(input())

promedio = (c_1 + c_2 + c_3 + c_4) / 4
print(f"Tu promedio es: {promedio: .10f}")
