'''
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.
'''

def area_rectangulo (base,altura):
    return base*altura

base = float(input('Introduce la base del rectángulo : '))
altura = float(input('Introduce la altura del rectángulo : '))

print(f'El area del rectángulo es {area_rectangulo(base,altura)}')