"""
Crea un método que calcule el costo de un envío con tarifas variables.
    - Tarifa base: $5 por kg.
    - Si el peso es > 10 kg, se añade un recargo de $10.
    - Si la distancia es > 500 km, se añade un 15% de recargo sobre el costo base.

Tú método no debe imprimir nada. En su lugar debe retornar el resultado y
posteriormente imprimir ese resultado en tu método main.
"""

COSTO_POR_KG: int = 5


def costo_envio(peso: float, distancia: float) -> float:
    costo_base = peso * COSTO_POR_KG
    total = costo_base

    if peso > 10:
        total += 10

    if distancia > 500:
        total += costo_base * 0.15

    return total


def main():
    peso = float(input("Peso: "))
    distancia = float(input("Distancia: "))
    print(costo_envio(peso=peso, distancia=distancia))


main()
