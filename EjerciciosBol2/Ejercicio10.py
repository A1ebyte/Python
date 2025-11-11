"""10. Modificar el programa anterior para que nos muestre al final la media aritmética de
las entradas válidas"""
numeros=[]
while True:
    try:
        opc=input("Ingresa un numero o termina con FIN: ")
        if opc.isdigit():
            if 0<=int(opc)<=100:
                numeros.append(int(opc))
            else:
                raise Exception
        else:
            if opc=="FIN":
                break
            raise Exception
    except:
        print("El valor ingresado no es valido")
print(f"Entradas validas: {len(numeros)}",f"Media aritmetica: {sum(numeros)/len(numeros)}",sep="\n")