"""14. Modifica el programa que validaba si un NIF era correcto comprobando si la letra que
incorpora lo es. La forma de hacerlo es la siguiente:"""
id = input("Escribe tu dni:\n").strip()
id=id.upper()
letraResto=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
dni=True
nie=True
if len(id)!=9:
    dni=False
    nie=False
if id[0:8].isdigit() and id[8].isalpha():
    nie=False
if id[1:8].isdigit() and id[0].isalpha() and id[8].isalpha() and id.startswith(("X","Y","Z")):
    dni=False
if dni:
    letra=int(id[0:8])%23
    dni=True if id[8]==letraResto[letra] else False
if nie:
    numero = "1" if id.startswith("Y") else "2" if id.startswith("Z") else "0"
    numero=numero+id[1:8]
    letra=int(numero)%23
    nie=True if id[8]==letraResto[letra] else False
print("Es un DNI valido" if dni==True and nie==False else "Es un NIE valido" if nie==True and dni==False else "No es valido")