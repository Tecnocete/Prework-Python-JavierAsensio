'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y 
determine si es mayor de edad (mayor o igual a 18 años) o no.
'''
mayoria_edad= 18
def es_adulto():
    try:
        edad = input('Indicanos tu edad con números: ')
        edad_corregida= int(edad)
        comprobante_edad = edad_corregida >= mayoria_edad
        print(comprobante_edad)
    except:
        print("El número no esta escrito con numeros")
        es_adulto()

es_adulto()
