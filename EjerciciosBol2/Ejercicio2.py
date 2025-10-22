"""2. Idem al anterior pero ordenando ahora en orden descendente"""
lista=[]
for x in range(0,3):
    lista.append(input("Escribe una palabra"))
lista.sort(reverse=True)
print(", ".join(lista))