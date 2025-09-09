"""
Factorial de un número
Calcular el factorial de un número N, donde N es solicitado al usuario.

El factorial de un número es:

Si N=0 o N=1, el factorial es 1

Si N es cualquier número positivo se calcula como  N = 1 * 2 * 3 * ... * N.

Por ejemplo:  factorial de 4 es 1*2*3*4 que es 24

Entrada

Un número entero mayor o igual a 0.

Salida

El valor (número entero positivo) correspondiente al factorial del número recibido.

O el mensaje "Factorial no definido para negativos"

Ejemplos de ejecución del programa

>>> 6

720
"""


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    res = 1
    while n > 1:
        res *= n  # res = res * n
        n -= 1

    return res


def main():
    n = int(input("N: "))
    print(factorial(n=n))


main()
