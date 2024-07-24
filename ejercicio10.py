'''

Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente 
a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''

dic_semana = {
    1:'lunes',
    2:'martes',
    3:'miércoles',
    4:'jueves',
    5:'viernes',
    6:'sábado',
    7:'domingo'
}
def dia_semana (num):
    return dic_semana[num]

num = int(input("Introduce el número del día de la semana: "))

print (f'El día de la semana correspondiente a {num} es el {dia_semana(num)}')
