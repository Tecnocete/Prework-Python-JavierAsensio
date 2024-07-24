'''

Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el usuario.
'''
def sumar_lista(lista):
    return sum(lista)
numeros = list(map(int,input('Introduce los numeros separados por comas:').split(',')))

print(sumar_lista(numeros))

