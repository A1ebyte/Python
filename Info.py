from mercurial.fileset import removed
from mpmath import extend

edad=56
print(edad)
edad='doce'
print(edad)
precio=54.6
booleano=True
MESES_ANO=12 #Noexisten constantes en python pero se escribe en Mayuscula y los espacios con _ para decir que lo es

print(5//3) #cociente
print(5%3) #resto/modulo
print(2**2) #elevado

nuevo=(precio + 5) * MESES_ANO
print(nuevo)

texto="hola"
texto+=" "+"mundo"
texto = texto+" o_0"
print(texto)
print(texto, edad, precio)
print(texto, edad, precio, end=" ***\n") #end cambia el ultimo character por el que pones ahi en este caso el \n y evita el salto de linea del siguiente print
print(texto, edad, precio, sep=" *** ") #sep cambia el separador que pone entre las variables con coma

numero='12'
numero= int(numero) +1 #casteo
print(numero)

if numero==13:
    print("hi")
elif numero==12:
    print("no se")
else:
    print("bye")

for n in range(0,10):
    print(n)

for n in range(10):
    print(n)

for _ in range(10): #si se pone _ en el for funciona y es cuando la var no se utilizara
    print("hi")

for n in range(0,10,2): #aqui el tercer valor es la cantidad de pasos que da
    print(n)

for n in range(10,0,-1): #recorrer for hacia atras
    print(n)

for n in "Hola bitch": #recorrer for hacia atras
    print(n)

print("Hola Mundo")

texto=input("\ndime algo: ")
newTexto=""
for n in texto:
    if not n.isspace():
        newTexto+=n
print(newTexto)
print(texto.replace(' ',''))  #remplazar todos
print(texto.replace(' ','',2))  #remplazar solo primeros tantos

i=0
while (i < 10): #los parentesis no son obligatorios
    print(i)
    i+=1

import random  #para poder hacer los randoms
print(random.randint(0,2))

pi=3.141592
print(round(pi,2))
print(round(pi,3))
print(round(pi,4))

texto2="Hola Mundo"
print(texto2[::-1])
print(texto2[1])
print(texto2[1:3])
print(texto2[1:6:2])

texto3="Hola","Mundo","Xd"  #Esto es una tupla es una coleccion unica de python

texto4=f"hola mundo {3} {texto2}"

for char in texto2:
    print(char)

print(texto2.upper()) #Mayuscula
print(texto2.lower())  #Minuscula
print(texto2.swapcase())  #Cambair Minuscula*Mayuscula
print(texto2.find("o"))    #Busca el 1er indice de lo que se busca
print(texto2.find("H"))
print(texto2.find("Hol"))
print(texto2.find("o",4))   #lo de arriba pero se indica desde donde empezar
print(texto2.count("o"))  #cuantas veces aparece lo q se busca

num=3
match num:
    case 2:
        print("a")
    case 3 | 4:   #un valor o el otro
        print("b")
    case _:   #defecto
        print("Por defecto")

 # a*b if a*b>0 else 0   Operador ternario

#Esto es un comentario linea
'''
comentario
de 
bloque
'''

if "Hola">"Holo":
    print("Hola es mayor")
else:
    print("Holo es mayor")

#Listas se pueden modificar, las tuplas no
lista1=[]
lista2=list()
lista3=[1,2,3,4,5,5]
lista4=["eva","adam","moha"]
lista5=[1,"2",3,"4",False,5,"Perez",[1,2,3],4.56]
lista6=[0,54,4,5111,2,124,8,21454,24,54]


lista5=lista1+lista2
print(lista5)

lista5.extend(list+lista3)
print(lista5++lista4)

lista5.append(10)
lista3.insert(1,333)
ele=lista5.pop()
lista5.removed("eva")
lista3.sorted(reverse=True)
print(lista2)

if 5 in lista1:
    print("si")
    print("Aparece",lista1.count(1),"veces")
    print("Aparece", lista1.index(1), "veces") #tira error si no esta en la lista
else:
    print("no")

text001="Hola Mundo Cruel"
lista7=list(text001)
print(lista7)
text002=str(lista7)
print(text002)

lista8=lista1[::-1]
print(lista8)
print(random.choice(lista4))   #elige aleatoriamente de la lista
print(random.sample(lista4,2))  #2 elementos random que no se repiten
random.shuffle(lista4) #desordena la lista