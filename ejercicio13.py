'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo o no.
'''

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    limite = int(numero**0.5) + 1
    for i in range(5, limite):
        if numero % i == 0:
            return False
    return True

num = int (input('Ingrese un numero que desea saber si es primo: '))

print (es_primo(num))
