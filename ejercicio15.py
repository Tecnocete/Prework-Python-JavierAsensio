'''

Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.

'''

def convertir_minutos_a_horas_minutos(minutos):
    horas = minutos//60
    minutos_resto= minutos%60
    return horas, minutos_resto
horas,minutos_resto=convertir_minutos_a_horas_minutos(180)
print (horas,minutos_resto)