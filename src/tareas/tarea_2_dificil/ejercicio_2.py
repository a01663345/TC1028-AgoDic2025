"""
Crea un método que convierta un número entero a número romano.

Entradas:
- El Número entero a convertir.
    - El número tendra un rango de 1 a 3999

Ejemplo de ejecución:
>>> 3749
MMMDCCXLIX

>>> 58
LVIII

>>> 1994
MCMXCIV
"""


# Solución sin arrays ni map
def next_symbol(value: int) -> tuple[str, int]:
    new_value = value - 1000
    if new_value >= 0:
        return "M", new_value

    new_value = value - 900
    if new_value >= 0:
        return "CM", new_value

    new_value = value - 500
    if new_value >= 0:
        return "D", new_value

    new_value = value - 400
    if new_value >= 0:
        return "CD", new_value

    new_value = value - 100
    if new_value >= 0:
        return "C", new_value

    new_value = value - 90
    if new_value >= 0:
        return "XC", new_value

    new_value = value - 50
    if new_value >= 0:
        return "L", new_value

    new_value = value - 40
    if new_value >= 0:
        return "XL", new_value

    new_value = value - 10
    if new_value >= 0:
        return "X", new_value

    new_value = value - 9
    if new_value >= 0:
        return "IX", new_value

    new_value = value - 5
    if new_value >= 0:
        return "V", new_value

    new_value = value - 4
    if new_value >= 0:
        return "IV", new_value

    new_value = value - 1
    if new_value >= 0:
        return "I", new_value


def int_to_roman(value: int) -> str:
    result = ""
    while value > 0:
        symbol, new_value = next_symbol(value=value)
        result += symbol
        value = new_value

    return result


def main():
    print(int_to_roman(value=int(input(""))))


if __name__ == "__main__":
    main()
