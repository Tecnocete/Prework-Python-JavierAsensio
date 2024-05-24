'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
'''
def contador_vocales(str_vocales):
    contador = 0
    vocales=['a','e', 'i', 'o', 'u']
    for i in str_vocales:
        if i in vocales:
            contador+=1
    return contador

frase = input('Añade el texto: ')
print (contador_vocales(frase))
