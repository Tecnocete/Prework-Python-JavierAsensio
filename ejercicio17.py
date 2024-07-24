'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.
'''

def conversor_distancia(distancia,magnitud):
    if magnitud == 'kilometros':
        return (f" {distancia} kilometros son {distancia/1.69034} millas")
    else:
        return (f"{distancia} millas son {distancia*1.69034} kilometros")

distancia = float(input('Introduzca la distancia deseada: '))
magnitud = input("introducza la magnitud (kilometros o millas): ")
print (conversor_distancia(distancia,magnitud))