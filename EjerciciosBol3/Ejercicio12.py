"""12. Las matrículas españolas constan de un número de cuatro dígitos y tres letras
cualesquiera en mayúsculas a excepción de las vocales, la Ñ y la Q. Escribe un
programa que detecte si una matrícula introducida por teclado es válida o no."""
matricula = input("Escribe tu matricula:\n").strip().upper()
valida=True
letrasExcepciones=["A","E","I","O","U","Ñ","Q"]
if len(matricula)!=7:
    valida=False
if not matricula[0:4].isdigit() or not matricula[4:7].isalpha():
    valida=False
for letra in matricula[4:7]:
    if letrasExcepciones.count(letra)>0:
        valida=False
        break
print("Es valido" if valida==True else "No valido")