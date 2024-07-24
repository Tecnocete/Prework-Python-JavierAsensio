'''
Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
'''

def contador_palabras(oracion):
    return len(oracion.split())

oracion= input('Introduce una frase: ')
print (contador_palabras(oracion))