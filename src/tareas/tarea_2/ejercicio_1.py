"""
Diseña una función que convierta una cantidad entre diferentes unidades de medida.
La función debe recibir la cantidad, la unidad de origen y la unidad de destino.
No necesitas manejar todos los casos, solo algunos ejemplos.
Si la combinación de unidades no es válida, devuelve -1.

Unidades disponibles:
'kg' (kilogramos)
'lb' (libras)
'km' (kilómetros)
'mi' (millas)

Fórmulas de Conversión:
1 kg = 2.20462 lb
1 km = 0.621371 mi

Ejemplo de Ejecución:
>>> 10
>>> kg
>>> lb

22.046

- - - -
>>> 50
>>> mi
>>> km

80.467

- - - -
>>> 100
>>> lb
>>> kg

45.359

- - - -
>>> 10
>>> kg
>>> km

-1
"""


def conversion(cantidad: float, unidad_origen: str, unidad_destino: str) -> float:
    if unidad_origen == "kg" and unidad_destino == "lb":
        return cantidad * 2.2

    if unidad_origen == "lb" and unidad_destino == "kg":
        return cantidad / 2.2

    if unidad_origen == "km" and unidad_destino == "mi":
        return cantidad * 0.62

    if unidad_origen == "mi" and unidad_destino == "km":
        return cantidad * 1.61

    return -1


def main():
    c: float = float(input("Cantidad: "))
    unidad_origen: str = input("Unidad origen: ")
    unidad_destino: str = input("Unidad destino: ")
    resultado = conversion(
        unidad_origen=unidad_origen, unidad_destino=unidad_destino, cantidad=c
    )

    print(resultado)


if __name__ == "__main__":
    main()
