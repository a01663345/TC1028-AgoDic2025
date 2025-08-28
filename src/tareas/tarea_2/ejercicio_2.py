"""
Diseña un programa que calcule el impuesto sobre la renta de una persona
basándose en un sistema de tramos progresivos. La función debe recibir el
ingreso anual y devolver el monto total del impuesto a pagar.

Reglas de Impuestos:
- Ingresos de $0 a $10,000: Tasa del 0%.
- Ingresos de $10,001 a $50,000: Tasa del 15% solo sobre la parte del ingreso
    que supera los $10,000.
- Ingresos de $50,001 a $100,000: Tasa del 20% sobre la parte del ingreso que
    supera los $50,000, más el impuesto total del tramo anterior
    (que es el 15% de $40,000).
- Ingresos mayores a $100,000: Tasa del 30% sobre la parte del ingreso que supera
    los $100,000, más los impuestos totales de los tramos anteriores.
"""
