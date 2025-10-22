datos=int(input("De cuantos segundos hablamos: "))
segundos=datos%60
minutos=datos//60
horas=datos//60**2
dias=horas//24
horas%=24
minutos%=60
texto=(f"{datos} segundos son {f"{dias} dias, " if dias!=0 else ""}{f"{horas} horas, " if horas!=0 else ""}"
       f"{f"{minutos} minutos, " if minutos!=0 else ""}{f"{segundos} segundos. " if segundos!=0 else ""}")
print(texto)