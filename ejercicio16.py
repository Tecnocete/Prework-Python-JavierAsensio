contador = {
    'pares': 0,
    'impares': 0
}

def contador_pares_impares(lista):
    for i in lista:
        try:
            numero = int(i)  
            if numero % 2 == 0:
                contador['pares'] += 1
            else:
                contador['impares'] += 1
        except ValueError:
           
            print(f"El elemento '{i}' no es un número válido y será ignorado.")
            continue
    return contador

lista = input("Introduce una lista de números separándolos por comas: ").split(",")
resultados = contador_pares_impares(lista)
print(resultados)

