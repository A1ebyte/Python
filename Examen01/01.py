numerosCapicua=[]
numero1=input("Escribe el primer numero: ")
numero2=input("Escribe el segundo numero: ")
if not numero1.isdigit() or not numero2.isdigit():
    print("Valores no validos")
    quit()
numero1=int(numero1)
numero2=int(numero2)
if numero1<0 or numero2<0:
    print("Valores no validos")
    quit()
if numero1>numero2:
    num=numero1
    numero1=numero2
    numero2=num
if numero1==numero2:
    numerosCapicua.append(str(numero1))
for x in range(numero1,numero2):
    if x<10:
        numerosCapicua.append(str(x))
    if 10 <= x < 100:
        unidades=int(str(x)[0])
        decimas=int(str(x)[1])
        if unidades==decimas:
            numerosCapicua.append(str(x))
    if x>100:
        numString=str(x)
        numStringReves=numString[::-1]
        if numString==numStringReves:
            numerosCapicua.append(str(x))
print(f"No hay ningun numero capicua entre {numero1} y {numero2}") if len(numerosCapicua)==0 \
    else print(f"Numeros capicuas entre {numero1} y {numero2}: {", ".join(numerosCapicua)}"
               f"\nHay un total de {len(numerosCapicua)} numeros capicuas")