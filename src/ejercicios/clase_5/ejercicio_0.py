def Suma(n1: int, n2: int) -> int:
    return n1 + n2


def Resta(n1, n2):
    return n1 - n2


def Multiplicacion(n1, n2):
    return n1 * n2


def Square(n):
    return n * n


def MuestraResultado(s, r, m) -> None:
    print("La suma de los números es:", s)
    print("La resta de los números es:", r)
    print("La multiplicación de los números es:", m)


def main() -> None:
    print("Operaciones Básicas")
    num1: int = int(input("Dame un número:"))
    num2: int = int(input("Dame otro número:"))

    suma = Suma(num1, num2)
    resta = Resta(num1, num2)
    multi = Multiplicacion(num1, num2)
    MuestraResultado(suma, resta, multi)


main()
