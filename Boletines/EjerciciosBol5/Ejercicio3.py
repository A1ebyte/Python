"""
3. Escribir un programa que cuenta las palabras que tiene una frase introducida
previamente por teclado. Las palabras pueden estar separadas por más de un espacio
pero siempre debe de haber al menos uno. No tenemos en cuenta los signos de
puntuación como separadores.
"""
frase = input("Introduce una frase: ")
palabras = frase.split()
cantidad = len(palabras)
print("La frase tiene", cantidad, "palabras.")
