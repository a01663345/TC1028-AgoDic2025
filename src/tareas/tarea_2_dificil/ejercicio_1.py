"""
Crea un método que devuelva un tablero de bingo
- Un tablero de bingo se conforma de una tabla de 5 filas por 5 columnas.
- Cada celda esta compuesta por un número aleatorio de 1 a 99
- Dicho número no se puede repetir.

Tú método no deberá devolver una de estas dos opciones:
- Una lista con los 25 números
- Una matriz (lista de listas), donde cada lista en la lista sea de 5 números

Adicionalmente deberás crear un segundo método llamado
imprime_tablero, que reciva la lista del primer método y la imprima de la
siguiente manera

11,  2,  33, 4, 5
 6, 99,  8,  9, 10
11, 12, 13, 14, 15
61, 17, 78, 19, 20
29, 90, 93, 24, 99

Es decir, 5 números por fila.
Importante: No importa si dejas espacios o no entre los números
pero si debe haber comas entre cada número y salto de línea entre cada fila.

Hint:
- Investiga el método ",".join(some_array)
- ¿Cómo sabrías que un número ya fue agregado al tablero?
    - Recuerda que un arreglo de 10 digitos tiene 0 index
    - Es decir, si tiene 10 elementos, los indices de tu arreglo van de 0-9
    - Si fuera de 22 elementos, tus indices van de 0 a 21.
    - ¿Crees que esto sea últil para resolver el problema?
"""

import random


def generate_board() -> list[int]:
    map = [False] * 100
    count = 0
    while count < 25:
        number = random.randint(1, 99)
        if not map[number - 1]:
            map[number - 1] = True
            count += 1

    return [idx + 1 for idx, val in enumerate(map) if val == True]


def print_board(items: list[int]) -> None:
    for i in range(5):
        row = []
        for j in range(5):
            item_index = i * 5 + j
            row.append(str(items[item_index]))

        print(", ".join(row))


def main():
    print_board(items=generate_board())


if __name__ == "__main__":
    main()
