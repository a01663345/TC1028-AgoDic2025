"""
Crea un método que dado un número de dos digitos,
genere la suma de sus digitos.

Ejemplo de ejecución:
>>> 99
18

>>> 10
1

>>> 27
9
"""


def suma_digitos(n: int) -> int:
    if n < 10 or n > 99:
        raise ValueError("Número no válido")

    return n // 10 + n % 10


def main():
    print(suma_digitos(n=int(input("Numero: "))))


if __name__ == "__main__":
    main()
