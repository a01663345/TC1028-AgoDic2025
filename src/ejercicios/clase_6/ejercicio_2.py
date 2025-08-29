"""
Crea un método que verifice si un año es bisiesto según las reglas del calendario.
- Un año es bisiesto si es divisible por 400
- O si es divisible por 4 pero no por 100

Tú método no debe imprimir nada. En su lugar debe retornar el resultado y
posteriormente imprimir ese resultado en tu método main.
"""


def es_bisiesto(year: int) -> bool:
    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False


def main():
    year = int(input("Dame el año: "))
    print(es_bisiesto(year=year))


main()
