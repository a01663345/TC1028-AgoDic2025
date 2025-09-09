"""
Tienes un conjunto de tres números enteros positivos, a, b, y c, donde se te
garantiza que uno de ellos es el producto de los otros dos. Escribe una función
llamada encontrar_numero_oculto que reciba estos tres números y devuelva el
número que es el producto.

Ejemplos:
Si la entrada es 2, 3, 6, la salida debe ser 6.
Si la entrada es 5, 4, 20, la salida debe ser 20.
Si la entrada es 10, 2, 5, la salida debe ser 10.
Si la entrada es 1, 10, 10, la salida debe ser 10.
"""


def encontrar_numero_oculto(a: int, b: int, c: int) -> int:
    if a * b == c:
        return c
    if a * c == b:
        return b
    if b * c == a:
        return a

    raise ValueError("Ninguno es el producto de los otros dos.")


def main():
    print(
        encontrar_numero_oculto(
            a=int(input("A: ")), b=int(input("B: ")), c=int(input("C: "))
        )
    )


if __name__ == "__main__":
    main()
