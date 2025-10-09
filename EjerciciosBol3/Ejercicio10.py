"""
10. Escribe un programa que valide si un NIF español introducido por teclado es correcto.
La longitud exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de
ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar
escrita en mayúsculas o minúsculas.
"""
dni = input("Escribe tu dni:\n").strip()
if len(dni)==9:
    if dni[0:8].isdigit():
        if dni[8].isalpha():
            print("Es valido")
        else:
            print("No es valido")
    else:
        print("No es valido")
else:
    print("No es valido")
