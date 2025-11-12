"""2. Incluye operaciones adicionales (raiz cuadrada, cuadrado, cubo, por ejemplo)"""
num1=int(input("Ingresa un numero: "))
num2=int(input("Ingresa el otro numero: "))
match input("Elige una opcion\n(S para suma, R para resta, M para multiplicar, D para dividir, E para elevar, RM para resto/modulo y RZ para raiz)\n").lower():
    case "s":
        print(num1+num2)
    case "r":
        print(num1-num2)
    case "m":
        print(num1*num2)
    case "d":
        print(num1/num2)
    case "e":
        print(num1**num2)
    case "rm":
        print(num1%num2)
    case "rz":
        print(num1**(1/num2))
    case _:
        print("No se puede hacer una operacion")