'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
def suma_numeros_pares(a=0,b=101):
    return sum([i for i in range (a,b,2)])
print (suma_numeros_pares())
    