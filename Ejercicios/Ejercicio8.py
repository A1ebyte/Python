"""8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
(puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
intereses de ningún tipo y redondeamos a dos decimales."""

precioPagar=input("Importe a pagar: ")
mesesPagar=input("Meses para pagar: ")
try:
    precioPagar=float(precioPagar)
    mesesPagar=int(mesesPagar)
except ValueError:
    print("El valor de Importe o Mes no valido")
else:
    print(f"Se debera pagar: {round(precioPagar/mesesPagar,2)} en un total de {mesesPagar} meses")