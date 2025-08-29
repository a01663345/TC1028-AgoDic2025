"""
Crea un método que calcule el precio final con un descuento del 10% si el precio
original es mayor a 100.

Tú método no debe imprimir nada. En su lugar debe retornar el resultado y
posteriormente imprimir ese resultado en tu método main.
"""


def calculo(precio: float) -> float:
    if precio <= 100:
        return precio

    return precio * 0.9


def main():
    precio: float = float(input("Precio: "))
    print(calculo(precio=precio))


if __name__ == "__main__":
    main()
