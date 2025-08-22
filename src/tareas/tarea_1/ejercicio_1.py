"""
Haz un programa sirva para calcular el precio que va a pagar un cliente por
comprar cemento.

El programa debe leer la cantidad de bultos de cemento que va a comprar el
cliente, y el precio del bulto de cemento.

El programa debe mostrar como salida 3 datos uno en cada renglón:
- el precio antes de impuestos,
- los impuestos (que son el 16% del precio)
- el total a pagar por el cliente.

Entrada
- La cantidad de bultos de cemento
- El precio por bulto de cemento

Salidas
- El precio antes de impuestos
- Los impuestos
- El total a pagar

Ejemplo de ejecución del programa:
>>5
>>180

Output:
900.0
144.0
1044.0
"""

n_bultos: int = int(input())
precio_bulto: int = float(input())

precio_antes_de_impuestos: float = n_bultos * precio_bulto
impuestos: float = precio_antes_de_impuestos * 0.16

print(precio_antes_de_impuestos)
print(impuestos)
print(precio_antes_de_impuestos + impuestos)
