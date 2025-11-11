"""4. Escribir un programa que nos pida una cadena por teclado y luego cuente cuantas
palabras hay en ella con cuatro o más vocales diferentes. Por ejemplo, si introducimos
la frase “Crisis constitucional por culpa del murcielago guineoecuatorial” Nos debería
de decir que 3. Tendrías que tener en cuenta que las vocales pueden ir en mayúsculas
o no y son la misma letra. Presupón que ninguna vocal va acentuada de ninguna
forma.
"""
frase = input("Introduce una frase: ")
frase = frase.lower()
vocales = "aeiou"
palabras = frase.split()
contador = 0

for palabra in palabras:
    vocales_en_palabra = set(letra for letra in palabra if letra in vocales)
    if len(vocales_en_palabra) >= 4:
        contador += 1
print("Número de palabras con 4 o más vocales diferentes:", contador)
