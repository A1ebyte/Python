try:
    fichero1=open('quijote.txt', "wt")# wt sobreescribe, at agrega al fichero
    fichero1.write("En un lugar de la Mancha, de cuyo nombre no quiero acordarme,\n")
    fichero1.write("no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.\n")

    lista=["Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados,\n",
           "lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.\n"]

    fichero1.writelines(lista)
    fichero1.close()
except FileNotFoundError:
    print("El fichero no existe")