"""
Ejercicio 3
Escribe una función que reciba como parámetro 2 números enteros y una clave que
es una letra.

La clave representa una operación aritmética de acuerdo con la siguiente tabla:

Clave Significado

s        Suma
r        Resta
m       Multiplicación
d        División

La función debe aplicar la operación aritmética a los 2 valores recibidos y
regresar como valor de retorno el resultado de dicha operación.

Nota que dentro de la función no mostrarás nada, solo regresarás el valor usando return.

Escribe ahora una función main en la que pidas al usuario teclear 2 valores
numéricos y una clave (s, r, m, d), después llama la función con los parámetros
correspondientes y luego muestra el resultado de la operación que regresó la función.

Entradas
valor 1
valor 2
clave

Salidas
El resultado de la operación que se especifica con la clave

Ejemplos de ejecución del programa
>>>5
>>>3
>>>r

>>>10
>>>2
>>>m
20
"""

def suma (num_1: int, num_2: int) -> int:
  return num_1 + num_2
  
def resta (num_1: int, num_2: int) -> int:
  return num_1 - num_2

def multiplicacion (num_1: int, num_2: int) -> int:
  return num_1 * num_2

def division (num_1: int, num_2: int) -> float:
  return num_1 / num_2

def main ():
  numero_1 = int(input('Ingresa tu primer número: '))
  numero_2 = int(input('Ingresa tu segundo número: '))
  clave = input('Clave: ')

  if clave == "s":
    print(f'La suma de ambos números es {suma ( num_1 = numero_1, num_2 = numero_2)}')
  elif clave == "r":
        print(f'La resta de ambos números es {resta ( num_1 = numero_1, num_2 = numero_2)}')
  elif clave == "m":
        print(f'La multiplicación de ambos números es {multiplicacion ( num_1 = numero_1, num_2 = numero_2)}')
  elif clave == "d":
    if numero_2 == 0:
        print("Error: no se puede dividir entre cero")
    else:
        print(f'La división de ambos números es {division(num_1=numero_1, num_2=numero_2)}')
  else:
    print('Clave inválida')
  
main()
