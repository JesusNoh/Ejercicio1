def main():
    print("Calculadora Simple")
    numero1 = float(input("Ingrese el primer número: "))
    operador = input("Ingrese un operador (+, -, *, /): ")
    numero2 = float(input("Ingrese el segundo número: "))

    if operador == '+':
        resultado = numero1 + numero2
        print("Resultado: ", resultado)
    if operador == '-':
        resultado = numero1 - numero2
        print("Resultado: ", resultado)
    if operador == '*':
        resultado = numero1 * numero2
        print("Resultado: ", resultado)
    if operador == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado: ", resultado)
        else:
            print("Error: No se puede dividir por cero.")
    if operador not in ['+', '-', '*', '/']:
        print("Operador no válido")

main()
