"""4. Solicita una nota entre el 1 y el 10 (sin decimales) y devuelve la calificación según la
siguiente escala: 1-2 Muy deficiente, 3-4 Insuficiente, 5 Suficiente, 6 Bien, 7-8 Notable,
9-10 Sobresaliente"""
nota = int(input("Introduce una nota entre 1 y 10: "))

calificaciones = [
    (range(1,3), "Muy deficiente"),
    (range(3,5), "Insuficiente"),
    (range(5,6), "Suficiente"),
    (range(6,7), "Bien"),
    (range(7,9), "Notable"),
    (range(9,11), "Sobresaliente")
]

for r, texto in calificaciones:
    if nota in r:
        print(f"Tu calificación es: {texto}")
        break
else:
    print("Error: la nota debe estar entre 1 y 10")
