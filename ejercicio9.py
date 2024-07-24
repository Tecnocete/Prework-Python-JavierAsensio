'''
Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
'''

def conversor_moneda(monto,moneda):
    if moneda == 'euro':
        return (f" {monto} euros son {monto/0.85} dolares")
    else:
        return (f"{monto} dolares son {monto*0.85} euros")

monto = float(input('Introduzca la cantidad deseada: '))
moneda = input("introducza la moneda (dolar o euro): ")
print (conversor_moneda(monto,moneda))