"""
Crea un programa que simule el lanzamiento de 4 monedas.
Si las cuatro monedas caen en la misma cara, el programa deberá imprimir "Ganaste"
De lo contrario el programa deberá imprimir "Perdiste".
"""

import random

r1 = random.randint(0, 1)
r2 = random.randint(0, 1)
r3 = random.randint(0, 1)
r4 = random.randint(0, 1)

res = r1 + r2 + r3 + r4
if res == 4 or res == 0:
    print(f"Ganaste: {r1}")
else:
    print(f"Perdiste: {r1}, {r2}, {r3}, {r4}")
