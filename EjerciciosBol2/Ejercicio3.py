"""3. Escribir un programa que pida un número por teclado al usuario que simule ser el
precio de un artículo y escriba el resultado de aplicarle el IVA del 21%. El resultado
debe de estar redondeado a dos decimales."""
valor=float(input("escribe valor"))
valor*=.21
valor=round(valor,2)
print(valor)