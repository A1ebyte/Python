conjunto1 = {"Ana","Pedro","Luis","Eva","Ana"}#* no lo almacena por orden, van variando en orden
#No permite tener dos mismas variables
print(conjunto1)
lista=["Ana","Pedro","Luis","Eva","Ana"]
conjunto2 = set(lista) # Otra forma de llamar y combierte una lista en un conjunto
print(conjunto2)

for nombre in conjunto1:# Se recorrer el conjunto asi
    print(nombre)

if "Ana" in conjunto1:  # sí un elemento esta en el conjunto
    print("Ana esta")

print(len(conjunto1))

conjunto1.add("Manuel") # Añadir elemento
print(conjunto1)
conjunto1.remove("Ana") # Eliminar elementos
print(conjunto1)
conjunto1.discard("Eustaquio")#* si eliminamos algo que no existe, da error. Pero con 'discard' si puede eliminar

print(conjunto1.pop()) #* Eliminamos el primero, nos lo recupera, pero de manera aletoria
conjunto3=conjunto1.copy() #crea una copia del conjunto

conjunto1.clear() #* Elimina los elementos del conjunto
print(conjunto1)

profesPrimero = {"Natalia","José María","Pedro","Yago"}
profesSegundo =  {"José María","Agustín","Puche","Pedro"}
print(profesPrimero & profesSegundo) #* intercepción, nos devuelve los dos profesores repitos en el conjunto, los comunes
print(profesPrimero | profesSegundo)#* la unión consegui todos pero se consigue una ves
print(profesSegundo - profesPrimero)#* la diferencia
print(profesPrimero - profesSegundo)#* quita los que se repite o lo que no estan el comúnç
intersecion = profesPrimero & profesSegundo #* devuelve otro conjunto
print(intersecion)
#*METODOS
print(f"metodos intersecion {profesPrimero.intersection(profesSegundo)}")
print(f"metodos union {profesPrimero.union(profesSegundo)}")
print(f"metodos diferencia {profesPrimero.difference(profesSegundo)}")
print(f"metodos diferencia al reves {profesSegundo.difference(profesPrimero)}")