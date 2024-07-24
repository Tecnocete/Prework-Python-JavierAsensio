'''
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def palindromo(word):
    return word==word[::-1]

frase= input('Introduce una palíndromo: ').lower()

while palindromo (frase) == False:
    print('Vuelve a intentarlo: ')
    frase= input('introduce una palíndromo: ')

print (f'Enhorabuena {frase} es un palíndromo')

       
    