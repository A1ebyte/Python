"""
8. Escribir un programa que reciba una cadena de texto por teclado y la muestre sin
vocales. Por ejemplo, si recibe la cadena “Hola Mundo” debería de devolver “Hl Mnd”.
"""
text = input("Escribe tu texto:\n")
text=text.replace("a","").replace("A","")
text=text.replace("e","").replace("E","")
text=text.replace("i","").replace("I","")
text=text.replace("o","").replace("O","")
print(text)