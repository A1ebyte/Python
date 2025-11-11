numero=13
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

for n in "Hola bitch"[::-1]: #recorrer for hacia atras
    print(n)

for i, nombre in enumerate("Patata"):
    print(f"{i} - {nombre}")

i=0
while (i < 10): #los parentesis no son obligatorios
    print(i)
    i+=1


num=3
match num:
    case 2:
        print("a")
    case 3 | 4:   #un valor o el otro
        print("b")
    case _:   #defecto
        print("Por defecto")

a=1
b=2
c=a*b if a*b>0 else 0   #Operador ternario el 0 puede ser None si no quiero nada
print(c)
