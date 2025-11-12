"""11. Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos
comunique, además de si es válido de que tipo es."""
id = input("Escribe tu dni:\n").strip()
dni=True
nie=True
if len(id)!=9:
    dni=False
    nie=False
if id[0:8].isdigit() and id[8].isalpha():
    nie=False
if id[1:8].isdigit() and id[0].isalpha() and id[8].isalpha() and id.upper().startswith(("X","Y","Z")):
    dni=False
print("Es un DNI" if dni==True and nie==False else "Es un NIE" if nie==True and dni==False else "No es valido")
