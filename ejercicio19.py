
'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
'''

def es_bisiesto(year):
    if year>0:
        if year % 400 == 0:
            return (f'El año {year} Es bisiesto')
        elif year % 100 == 0:
            return (f'El año {year} no bisiesto')
        elif year % 4 ==0:
            return (f'El año {year} Es bisiesto')
        else:
            return (f'El año {year} no bisiesto')
    else:
        print('El numero ingresado no es correcto')
        

year = int(input('Introduce el año deseado con numeros: '))

print(es_bisiesto(year))
    
