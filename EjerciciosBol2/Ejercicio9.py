"""Escribir un programa que pida números entre el 1 y el 100 por teclado hasta que
escribamos la palabra FIN (con mayúsculas). Si el usuario introduce una entrada
inválida (números superiores a 100, otras cadenas de caracteres que no sean FIN, etc.)
no se tendrá en cuenta pero se mostrará un mensaje de error y el programa seguirá
su curso. Cuando terminamos (al introducir la palabra FIN, recuerda) mostraremos por
pantalla el numero de entradas válidas que hemos hecho (sin contar esta última
que sólo sirve para finalizar el programa)
"""
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
print(f"Entradas validas: {len(numeros)}")