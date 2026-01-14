"""EJERCICIO CON FORMATO DE EXAMEN
Escribir un programa que reciba un texto y devuelva un diccionario o una estructura similar donde las
palabras del texto serán las claves y el número de veces que aparece cada una de ellas su valor.
Considera que la frase que introducimos no tiene signos de puntuación, que el único separador entre
palabras son los espacios y no tengas en cuenta las tildes ni mayúsculas. Es decir: “qué” se
considera una palabra diferente de “que” y “Como” es distinta de “como”.
El texto debe de introducirse desde el teclado
EJEMPLO DE EJECUCIÓN:
Introduce tu texto: Como quieres que te quiera si el que quiero que me quiera no me quiere
como quiero que me quiera
Diccionario: {'Como': 1, 'quieres': 1, 'que': 4, 'te': 1, 'quiera': 3, 'si': 1, 'el': 1, 'quiero': 2, 'me': 3,
'no': 1, 'quiere': 1, 'como': 1}"""

def contar_palabras():
    texto = input("Introduce tu texto: ")
    palabras = texto.split()
    diccionario = {}

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    print("Diccionario:", diccionario)


# PROGRAMA PRINCIPAL
contar_palabras()
