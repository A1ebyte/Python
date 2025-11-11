#Se puede concatenar con , que pondran espacios por defecto
print("Hola", "mundo", "cruel")
#Y como siempre
print("Hola"+"mundo"+"cruel")

#para cambiar el separador hay que poner sep en defecto es " "
print("Hola", "mundo", "cruel",sep="-")

#para cambiar el ultimo caracter hay que poner end en defecto es \n
print("Hola", "mundo", "cruel",end=" ^w^\n")

texto2="Hola Mundo"
print(texto2[::-1]) #Para mostra el string al revés
print(texto2[1]) #elegir el character en esa posición
print(texto2[1:3]) #Hacer un subString desde la posición 1 hasta la 3 no incluida
print(texto2[1:-3]) #Hacer un subString desde la posición 1 hasta el final -3 posiciones sin incluir la ultima
print(texto2[1:6:2]) #Hacer un subString desde la posición 1 hasta la 6 no incluida dando pasos de a 2

#las comillas diabólicas de js aquí se hacen poniendo f antes del string (f"{param}")
texto4=f"hola mundo {3} {texto2}"

#Asi recorremos un string con un for
for char in texto2:
    print(char)

#Asi recorrer for hacia atras
for n in texto2[::-1]:
    print(n)

print(texto2.upper()) #Mayuscula
print(texto2.lower())  #Minuscula
print(texto2.swapcase())  #Cambair Minuscula*Mayuscula
print(texto2.find("o"))    #Busca el 1er indice de lo que se busca
print(texto2.rfind("o"))    #Busca el ultimo indice de lo que se busca, lo de find funciona con este
print(texto2.find("H")) #Si no lo consigue tira un -1
print(texto2.index("H")) #como el find pero de no conseguir lo que busca tira un ValueError
print(texto2.rindex("o")) #como el rfind pero de no conseguir lo que busca tira un ValueError
print(texto2.find("Hol"))
print(texto2.find("o",4))   #lo de arriba pero se indica desde donde empezar
print(texto2.count("o"))  #cuantas veces aparece lo que se busca
print("h o l a".split(" ")) #crea una lista apartir del separador
print("h o l a a d i o s".split(" ",4)) #decidimos cuantes veces se puede separar
print("5".zfill(4)) #rellena el string a la izquierda con 0 hasta llegar a la longitud
print("    0-o    ".strip()) #remueve todos los characters vacios al inicio y final, pones uno hay y removera esos
print("-    0-o    -".strip("-"))

print("123".isdigit()) #Si los valores son digitos
print(" ".isspace()) #Si es espacio
print("a1".isalnum()) # si es alpha numerico, es decir numeros y letras
print("asd".isalpha()) # si son letras
print("adios".islower()) # si esta en minúscula
print("ADIOS".isupper()) # si esta en mayúscula
print(texto2.startswith("h"))  #si empieza con ese character
print(texto2.endswith("o"))  # si termina con ese character

print("Texto a hacer replace :3".replace(' ',''))  #remplazar todos
print("Aqui solo quiero reemplazar 2 espacios".replace(' ','',2))  #remplazar solo los primeros tantos que se digan

#podemos comparar strings para saber cuál va antes que el otro
if "Hola">"Holo":
    print("Hola va despues Holo")
else:
    print("Holo va despues que Hola")

cadena = "1010101"
solo_binario = all(c in '01' for c in cadena)
print(solo_binario)  # True

palabras = ["python", "java", "html", "css", "C"]
largas = [p for p in palabras if len(p) > 3 and p.islower()]
print(largas)  # ['python', 'java', 'html', 'css']