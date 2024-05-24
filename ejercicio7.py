'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples 
(suma, resta, multiplicación, división) según la elección del usuario.
'''
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def pedir_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    print("Programa de operaciones aritméticas")
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicación")
    print("4: División")
    
    while True:
        try:
            opcion = int(input("Seleccione una operación (1-4): "))
            if 1 <= opcion <= 4:
                break
            else:
                print("Por favor, ingrese un número entre 1 y 4.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    num1 = pedir_numero("Ingrese el primer número: ")
    num2 = pedir_numero("Ingrese el segundo número: ")
    
    if opcion == 1:
        resultado = sumar(num1, num2)
    elif opcion == 2:
        resultado = restar(num1, num2)
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
    elif opcion == 4:
        resultado = dividir(num1, num2)
    
    print("El resultado es:", resultado)

# Llamada a la función principal
if __name__ == "__main__":
    main()
