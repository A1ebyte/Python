"""Escribir un programa que nos pida las notas obtenidas en un trimestre y nos muestre
la media ponderada sabiendo que;
1. La primera nota corresponde al trabajo en clase y cuenta como un 5% del total
2. La segunda corresponde a los ejercicios prácticos: 15%
3. La tercera la nota del examen: 80%
El resultado debería de mostrarse de dos formas: redondeado con dos decimales
(nota real) y sin redomdeada sin decimales (nota de boletín).
"""
notas=[]
porcentajes=[.05,.15,.8]
notaFinal=0
for x in range(1,4):
    notas.append(float(input(f"Escribe tu {x} nota")))
for x in range(len(notas)):
    notas[x]*=porcentajes[x]
print(f"Nota real:{round(sum(notas),2)}")
print(f"Nota boletin:{int(sum(notas))}")