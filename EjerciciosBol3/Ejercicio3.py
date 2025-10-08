"""
3. Escribir un programa que nos pida nuestro nombre y apellidos (dos peticiones
diferentes hechas en ese orden) y nos lo escriba formateado de la siguiente forma:
Morales Vázquez, José María
"""
name = input("Escribe tu nombre:\n")
lastname = input("Escribe tus apellido:\n")
print(lastname,name,sep=", ")
