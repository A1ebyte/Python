try:
    fichero1=open('quijote.txt', "rt")  #abre el fichero
    texto1=fichero1.readline() #lee una linea si no se pasa argumentos, con un numero en argumetnos lee esa cantidad de char
    print(texto1)
    fichero1.close()  #cierra el fichero
    print(f"*"*40+"\n")

    fichero1=open('quijote.txt', "rt")  #abre el fichero
    texto1=fichero1.readline() #lee una linea si no se pasa argumentos, con un numero en argumetnos lee esa cantidad de char
    while texto1!="":
        if texto1[-1]=="\n":
            print(texto1[:-1])
        else:
            print(texto1)
        texto1=fichero1.readline()
    fichero1.close()  #cierra el fichero
    print(f"*"*40+"\n")

    fichero2=open('quijote.txt', "rt")  #abre el fichero
    texto2=fichero2.read() #lee el fichero entero
    print(texto2)
    fichero2.close()  #cierra el fichero
    print(f"*"*40+"\n")

    fichero3=open('quijote.txt', "rt")  #abre el fichero
    texto3=fichero3.readlines() #para decirle cuantas lineas leer
    print(texto3)
    fichero3.close()  #cierra el fichero
except:
    print("error")

