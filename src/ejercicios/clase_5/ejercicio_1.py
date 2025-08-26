"""
Escribe una función llamada equivalente que reciba como parámetro una cantidad
de horas, minutos y segundos y regrese como valor de retorno el tiempo
equivalente en segundos.

Por ejemplo:
Si la función recibe los valores horas = 2, minutos = 20 y segundos = 8,
regresará el valor 8408.

Nota que la función no mostrará nada, solo regresa como valor de retorno la
cantidad de segundos equivalente.

Ahora escribe una función main en la que pidas al usuario teclear cuanto tiempo
en horas, minutos y segundos han tardado 2 procesos, después de pedir el tiempo
que dura cada proceso muestra el tiempo equivalente en segundos de dicho proceso.

Entradas
horas, minutos y segundos que tardó el proceso 1
horas, minutos y segundos que tardó el proceso 2

Salidas
Tiempo en segundos que tardó el proceso 1
Tiempo en segundos que tardó el proceso 2

Ejemplos de ejecución del programa:

>>>3
>>>15
>>>22
11722


>>>1
>>>10
>>>15
4215
"""


def equivalente_en_segundos(horas: int, minutos: int, segundos: int) -> int:
    horas_en_segundos = 3600 * horas
    minutos_en_segundos = 60 * minutos

    return horas_en_segundos + minutos_en_segundos + segundos


def main():
    user_input = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    resultado = equivalente_en_segundos(
        horas=user_input, minutos=minutos, segundos=segundos
    )
    print(resultado)


main()
