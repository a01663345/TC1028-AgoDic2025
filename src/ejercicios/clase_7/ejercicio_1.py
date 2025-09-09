"""
Escribe un programa que imprima los números de forma ascendente
en un rango dado por el usuario.

Ejemplo de ejecución:
>>> -1
>>> 4

-1
0
1
2
3
4
- - - -

>>> -2
>>> -4

-4
-3
-2
"""


def imprime_rango(inicio: int, fin: int) -> None:
    start = min(inicio, fin)
    end = max(inicio, fin)

    while start <= end:
        print(start)
        # start = start + 1
        start += 1


def main():
    inicio: int = int(input("Inicio:"))
    fin: int = int(input("Fin:"))
    imprime_rango(inicio=inicio, fin=fin)


main()
