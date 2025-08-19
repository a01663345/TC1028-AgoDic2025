"""
Una compañía de telefonía celular cobra $0.80 por mensaje, por mega o por minuto.
Realiza un programa que calcule el costo total mensual de un usuario según estos
datos.

Entradas:
El número de mensajes (número entero), el número de megas (número flotante) y el
número de minutos (número entero).
UN DATO POR LÍNEA Y EN ESE ORDEN.

Salidas:
Un número que representa el costo mensual.
"""

PRICE: float = 0.80
n_mensajes: int = int(input())
n_mbs: float = float(input())
n_minutos: int = int(input())

resultado: float = (n_mensajes + n_mbs + n_minutos) * PRICE
imprimir: str = f"Tu consume fue de: {resultado}"
print(imprimir)
