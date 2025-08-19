""" """

import math

radio: float = float(input("Radio: "))

area: float = 4 * math.pi * radio * radio
volumen: float = (area * radio) / 3

print(f"Area: {area: .2f}")
print(f"Volumen: {volumen: .2f}")
