"""3. Pide al usuario un número del 1 al 12 y muestra el nombre del mes correspondiente.
Muestra un error si el número no se corresponde con ningún mes"""

MESES=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
opc=input("Escribe el numero del mes")
try:
    print(MESES[int(opc)-1])
except:
    print("Error")

match input("Escribe el numero del mes"):
    case "1":
        print("Enero")
    case "2":
        print("Febrero")
    case "3":
        print("Marzo")
    case "4":
        print("Abril")
    case "5":
        print("Mayo")
    case "6":
        print("Junio")
    case "7":
        print("Julio")
    case "8":
        print("Agosto")
    case "9":
        print("Septiembre")
    case "10":
        print("Octubre")
    case "11":
        print("Noviembre")
    case "12":
        print("Diciembre")
    case _:
        print("El valor no corresponde con ningún mes")