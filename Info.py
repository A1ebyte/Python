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
print(texto.replace(' ',''))

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

#Esto es un comentario linea
'''
comentario
de 
bloque
'''