#19. Escribir un programa que pida un número por teclado y nos muestre sus divisores
eleccion=input("numero para saber sus divisores: ")
if not eleccion.isdigit():
    print("El numero ingresado no es un numero")
    quit()
eleccion=int(eleccion)
cociente=100
dividendo=1
divisores=[]
while dividendo<cociente:
    if eleccion%dividendo==0:
        cociente = eleccion//dividendo
        divisores.append(cociente)
        divisores.append(dividendo)
    dividendo=dividendo+1
divisores.sort()
print(f"Los divisores son {divisores}")