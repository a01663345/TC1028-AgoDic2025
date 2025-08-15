"""
Escribe un programa que:
Dado la hora actual, sin minutos. Quieres averiguar que hora será en x horas.

Por ejemplo, si actualmente son las 17 horas, y quieres sabes que hora será 
dentro de 9 horas.

En el caso anterior, en 9 horas serán las 02 a.m.

Entradas:
- La Hora Actual (Un entero de 0 a 24)
- Las horas a agregar (Un entero)

Salidas:
- La hora que sera dentro de x horas (Un número de 0 a 24)
"""
hora_actual = int(input())
x_horas = int(input())

resultado = (hora_actual + x_horas) % 24
print(f"Seran las {resultado} en {x_horas} horas.")
