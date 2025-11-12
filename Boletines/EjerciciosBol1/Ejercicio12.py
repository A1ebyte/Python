import random
dadosCant=input("Cuantos dados tiro: ")
dadosCaras=input("Cuantas caras tienen los dados: ")
CARAS=[4,6,8,12]
'''try:
    dadosCaras=int(dadosCaras)
    dadosCant=int(dadosCant)
except ValueError:
    print("Datos Invalidos")
else:
    if dadosCaras in CARAS:
        for _ in range(dadosCant):
            print(random.randint(1,dadosCaras))
    else:
        print("No hay dados con esa cantidad de caras")'''

if dadosCaras.isdigit() and dadosCaras.isdigit():
    dadosCaras=int(dadosCaras)
    dadosCant=int(dadosCant)
    if dadosCaras in CARAS:
        for _ in range(dadosCant):
            print(random.randint(1,dadosCaras))
    else:
        print("No hay dados con esa cantidad de caras")
else:
    print("Datos Invalidos")
