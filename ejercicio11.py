'''

Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.

'''
from datetime import datetime

def calculadora_edad(anio):
    return datetime.now().year-anio

print (calculadora_edad(1956))