"""1. Vamos a hacer una pequeña calculadora. Solicita dos números al usuario y luego que
escriba la operación que quiere hacer (S para suma, R para resta, M para multiplicar y D
para dividir). Realiza la operación con un switch.
"""
num1=int(input("Ingresa un numero: "))
num2=int(input("Ingresa el otro numero: "))
match input("Elige una opcion\n(S para suma, R para resta, M para multiplicar y D para dividir)\n").lower():
    case "s":
        print(num1+num2)
    case "r":
        print(num1-num2)
    case "m":
        print(num1*num2)
    case "d":
        print(num1/num2)
    case _:
        print("No se puede hacer una operacion")