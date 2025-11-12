"""
4. Escribir un programa que pida por teclado una cadena de texto y la escriba en sin
espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios
que ha encontrado y suprimido.
"""
text = input("Escribe tu texto:\n")
cont=text.count(" ")
text=text.replace(" ","")
print(text, "Totales espacios blancos:",cont)
