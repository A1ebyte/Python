"""
Escribir un programa en python que guarde en un diccionario los precios de las frutas de la siguiente
tabla:
_____________________________
|  Fruta    | Precio (€/Kg) |
| Aguacate  |      4.35     |
| Mandarina |      2.60     |
|    Kiwi   |      3.75     |
|  Naranja  |      1.80     |
-----------------------------
NOTA: El diccionario debes de crearlo en el código del programa con los datos listados en la tabla
Tú programa debe de preguntar al usuario por una fruta y un número de kilos y mostrar por pantalla el
precio de ese número de kilos de fruta con dos decimales. El número de kilos debe de admitir
decimales. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. Captura
las posibles excepciones.
El programa finalizará cuando se escriba la palabra fin (de forma insensible a mayúsculas y/o minúsuculas)
EJEMPLO DE EJECUCIÓN:
¿Qué fruta quieres comprar? Sandía
Lo siento mucho pero no vendemos esa fruta
¿Qué fruta quieres comprar? Kiwi
¿Cuantos kilos quieres? ff
No has introducido bien la cantidad que quieres
¿Qué fruta quieres comprar? Mandarina
¿Cuantos kilos quieres? 4.75
4.75 de Mandarina cuestan 12.35 €
¿Qué fruta quieres comprar? fin
"""

def programa_frutas():
    frutas = {
        "aguacate": 4.35,
        "mandarina": 2.60,
        "kiwi": 3.75,
        "naranja": 1.80
    }

    while True:
        fruta = input("¿Qué fruta quieres comprar?\nPara salir escribir fin \n")

        if fruta.lower() == "fin":
            break

        fruta_lower = fruta.lower()

        if fruta_lower not in frutas:
            print("Lo siento mucho pero no vendemos esa fruta")
            continue

        try:
            kilos = float(input("¿Cuantos kilos quieres? "))
            precio = kilos * frutas[fruta_lower]
            print(f"{kilos} de {fruta.capitalize()} cuestan {precio:.2f} €")
        except ValueError:
            print("No has introducido bien la cantidad que quieres")


# PROGRAMA PRINCIPAL
programa_frutas()
