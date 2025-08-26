"""
Escribe una función llamada areaRect que reciba como parámetro el largo y ancho
de un rectángulo y que regresa como valor de retorno el área del rectángulo.

Escribe una función llamada perimetroRect que reciba como parámetro el largo y
ancho de un rectángulo y que regresa como valor de retorno el perímetro del rectángulo.

Observa que dentro de las funciones no mostrarás nada, solo regresarás el valor
calculado usando return.

Escribe ahora una función main que pregunte al usuario el largo y ancho del
rectángulo y después pregunte si quiere calcular el área o el perímetro del
rectángulo (pide una clave a para área y p para perímetro) y
después muestre el valor correspondiente al cálculo que pidió el usuario.

Entrada
largo del rectángulo
ancho del rectángulo
clave que indica qué se quiere calcular a - área o p - perímetro

Salida
El área o el perímetro del rectángulo, de acuerdo con la clave que se haya tecleado
Ejemplos de ejecución del programa

>>>10
>>>5
>>>a
50.0

>>>10
>>>3
>>>p
26.0
"""

import math


def area_rect(largo: float, ancho: float) -> float:
    return largo * ancho


def perimetro_rect(largo: float, ancho: float) -> float:
    return 2 * largo + 2 * ancho


def main():
    l = float(input("Largo: "))
    w = float(input("Ancho: "))
    clave = input("Clave: ")

    if clave == "a":
        print(f"El area es {area_rect(largo=l, ancho=w)}")
    elif clave == "p":
        res = perimetro_rect(largo=l, ancho=w)
        print(f"El perimetro es {res}")
    else:
        print("Opción no válida")


main()
