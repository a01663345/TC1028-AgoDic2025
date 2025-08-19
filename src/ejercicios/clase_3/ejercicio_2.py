"""
Escribe un programa que calcule la población de una especie en un determinado 
número de años. Utiliza la fórmula Ni * (e^rt), donde 
- Ni es la población inicial, 
- r es la tasa de crecimiento, la cual siempre es un número entre 0 y 1, 
- t es el tiempo en años
- e la constante de Euler.

Entrada
Tres números recibidos uno en cada renglón, correspondientes a: 
- población inicial (entero positivo), 
- tiempo en años (entero positivo) 
- tasa de crecimiento (flotante entre 0 y 1)

Salida
Un número entero, resultado del cálculo de la población final. 

IMPORTANTE: Trunca los decimales del número resultante, para que el resultado 
sea entero 
(¿Cuál es la función de la librería math de Python que te puede ayudar a truncar los decimales?).

Ejemplo de ejecución del programa:
>>> 100  
>>> 1
>>> 0.5

164
"""