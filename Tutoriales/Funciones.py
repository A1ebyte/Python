#Para crear metodos/funciones se hace
#los metodos siempre tienen que ir arriba, no puedes ponerlo abajo y llamarlo desde arriba
def miFuncion():
    #aqui dentro se pone lo que quieras hacer
    print("hola")

miFuncion()

#pasandole parametros
def miFuncionMsj(mensaje):
    print(mensaje)

miFuncionMsj("Pepe Grillo hola")

def miFuncionSaludo(nombre,mesj):
    print(f"Hola {nombre}, {mesj}")

#al poner los parametros como en otros lenguajes se pasan en orden, pero tambien se puede poner desordenadamente poniendo cual es el valor del parametro
print(miFuncionSaludo("Pepep","Ktal"))
print(miFuncionSaludo(mesj="que tal",nombre="KK"))

#Devolviendo un valor
def miFuncionReturn():
    return "See You Later Alligator"

print(miFuncionReturn())

#Aqui le ponemos que le pasaremos varios valores y esto los convertira en tupla
def miFuncionTodosArgQuequiera(*Num):
    for x in Num:
        print(x)

def muestraProfe(*nombres): #Meter un número de variable posible
    print(nombres) #los muestra como tupla

muestraProfe("Pedro","José María","Ana","Puche")

#Tambien puede devolver mas de un valor
def miFuncionReturnVarios():
    return "If you're lucky, rubber ducky!","Sayōnara, carbonara!"
#aqui decimos que los valores los guarde en n1 y n2
n1,n2=miFuncionReturnVarios()
print(n1,n2,sep="\n")
#print(" ".join(miFuncionReturnVarios())) #como devuelve una tupla podemos hacer el join

#asi se veria sin la funcion
nn,nm,nj=(1,22,3)
print(nn,nm,nj)

#Se les pune poner a los parametros valores por defecto
def valorRetorno2(nombre,despedida = " te veo pronto!"):
    return "Hola " + nombre + despedida

nombre = "José María"
print(valorRetorno2(nombre, " Que te vaya bien"))
print(valorRetorno2("Antonio")) #* coje el valor por defecto

#al llamar la funcion y pasarle una lista/etc... para desempaquetarla usamos el * antes del valor y asi se le pasa varios valores
def repitreNombre(veces,nombre):
    for _ in range(veces):
        print(nombre,end=" *** ")

datos = [2,"pepe"]
datos2 = [4,"Luis"]
repitreNombre(*datos)
repitreNombre(*datos2)
repitreNombre(*[3,"eva"])

#los parametros que se pasan son solo valores, mientras que si se pasa una lista/array/etc.. se pasa una referencia y esta si edita la original
