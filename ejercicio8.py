'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
def IMC (peso,altura):
    return peso/(altura/100)**2

def pedir_peso(a):
    while True:    
        try:
            return float(input(a))
        except:
            raise ('Introduce un número valido')
