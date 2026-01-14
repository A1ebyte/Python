"""
6. EJERCICIO CON FORMATO DE EXAMEN
Realiza un programa que lea una frase y nos diga si es un palíndromo o no. Un palíndromo es
una palabra o frase que se lee igual hacia adelante que hacia atrás sin tener en cuenta los
espacios en blanco ni que los caracteres tengan tilde o estén en mayúsculas.
Ejemplos de palíndromos:
La ruta nos aporto otro paso natural
Atale demoníaco Cain o me delata
Para facilitar la codificación se deberán introducir las frases sin tildes, pero si hay que tener
en cuenta las mayúsculas y los espacios. Tampoco tendrán signos de puntuación
Ejemplo de funcionamiento:
Introduce un texto: Dabale arroz a la zorra el abad
El texto introducido es un palíndromo
No hace falta comprobaciones sobre la entrada (que siempre será una cadena de texto, pero
si que es preciso vigilar que a veces puede que haya mas de un espacio entre las palabras o
incluso al principio y al final de la frase
"""

# Dabale arroz a la zorra el abad es palindromo

def es_palindromo(frase):
    # Eliminamos espacios y convertimos a minúsculas
    frase_limpia = ''.join(frase.split()).lower()
    frase_limpia = frase_limpia.replace('á', 'a').replace('é', 'e').replace('í', 'i')
    frase_limpia = frase_limpia.replace('ó', 'o').replace('ú', 'u')
    return frase_limpia == frase_limpia[::-1]

texto = input("Introduce un texto: ")
if es_palindromo(texto):
    print("El texto introducido es un palíndromo")
else:
    print("El texto introducido no es un palíndromo")
