"""6. Modifica el ejercicio anterior para que la nota del boletín se redondee
matemáticamente si es superior a 5 pero se trunquen los decimales si es inferior a 5
"""
notas=[]
porcentajes=[.05,.15,.8]
notaFinal=0
for x in range(1,4):
    notas.append(float(input(f"Escribe tu {x} nota")))
for x in range(len(notas)):
    notas[x]*=porcentajes[x]
print(f"Nota real:{round(sum(notas),2)}")
print(f"Nota boletin:{int(sum(notas)) if sum(notas)<=5 else round(sum(notas))}")