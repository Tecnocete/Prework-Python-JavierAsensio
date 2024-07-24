'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
def IMC (peso,altura):
    return round(peso/altura**2,2)

peso =  float(input("Introduce tu peso en kg: "))
altura =  float(input("Introduce tu altura en metros: "))

print(IMC(peso,altura))