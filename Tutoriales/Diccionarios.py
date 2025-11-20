#Crear diccionarios
dict1={}
dict2=dict()
dict3={"nombre": "jose","edad":57,"activo":True}
dict4=dict(color="azul",modelo="caddy",submodelo="Outdoor",motor=2.5)
dict5={1:"nombre",2:"apellido",3:"genero"}
print(dict1)
print(dict3)

#Obtener valor usando la clave
print(dict5[1])  #con los corchetes devuelve error
print(dict4["color"])
print(dict3.get("nombre"))  #si no existe la clave me devuelve un None
print(dict3.get("nombri",0))  #si no existe nos devuelve el valor de la derecha por defecto

#Recorre las claves
for ele in dict4.keys():
    print(ele)

for ele in dict4:
    print(ele)

#recorre los valoes
for ele in dict4:
    print(dict4[ele])

dict4.keys() #devuelve las llaves
dict4.values() #devuelve los valores
dict4.items()  #devuelve las 2 cosas como tupla

#agregar/sustituir valores
dict5[4]="pronombres"
print(dict5.items())
dict5[4]="nada"
print(dict5.items())

#fusionar diccionarios
dict3.update({"nombre": "Carlos","edad":35,"activo":True,"niños":2})
print(dict3.items())

#eliminar de un diccinario
dict1.clear()  #limpia el diccionario
dict3.pop("nombre") #por la clave se elimina, devuelve el valor del que se elimina
print(dict3.items())
dict3.popitem() #elimina el ultimo que se agrego al diccionario, devuelve una tupla con la clave-valor