"""
Escribe una función llamada convertir_temperatura que reciba un valor de
temperatura en grados Celsius.

La función debe convertir este valor a su equivalente en grados
Fahrenheit y Kelvin, y devolver ambos valores.

F = (C x 9/5) + 32
K = C + 273.15

Ejemplos:
- Si la entrada es 20, la salida debe ser (68.0, 293.15).
- Si la entrada es 0, la salida debe ser (32.0, 273.15).
"""


def convertir_temperatura(temperatura: float) -> tuple[float, float]:
    farenheit = (temperatura * (9 / 5)) + 32
    kelvin = temperatura + 273.15

    return farenheit, kelvin


def main():
    temperatura = float(input("Temperatura: "))
    f, k = convertir_temperatura(temperatura=temperatura)
    print(f, k)
    print(convertir_temperatura(20))
    print(convertir_temperatura(0))


main()
