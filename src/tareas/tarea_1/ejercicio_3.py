"""
Un caracol de un terrario de una primaria pública corre a 5.7 mm/s. Realiza un
programa para indicar cuántos centímetros recorrerá el caracol en una cantidad
de minutos dada por el usuario.

Entradas
Un número decimal que representa los minutos.

Salidas
Un número decimal que indica los centímetros recorridos.

Ejemplo de ejecución:
>>> 1

Salida
34.2
"""

VELOCIDAD = 5.7

minutos_en_segundos = int(input()) * 60
distancia_en_milimetros = 5.7 * minutos_en_segundos

print(distancia_en_milimetros / 10)
