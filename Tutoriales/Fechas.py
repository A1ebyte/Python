from datetime import date, time, datetime, timedelta

hoy=date.today()
ahora=datetime.now()
print(hoy)
print(ahora)

cumpleanos=date(year=1998,month=6,day=4)
despertador=time(hour=7,minute=30,second=15)
vacaciones=datetime(year=2025,month=12,day=19,hour=14,minute=20)
print(vacaciones)
print(cumpleanos)
print(despertador)

now=datetime.now()
nowformat1=now.strftime("%d/%m/%Y %H:%M:%S")
nowformat2=now.strftime("%d/%m/%Y %-H:%-M:%-S") #con él menos (-) significa que no queremos ceros a la izquierda
nowformat3=now.strftime("%a %d/%m/%Y") #la a es el dia de la semana abreviado y A completo
nowformat4=now.strftime("%d/%m/%y") #la y en minúscula solo 2 dígitos en mayúscula 4 dígitos
nowformat5=now.strftime("%a/%B/%y") #la B da el nombre del mes completo y b abreviado
nowformat6=now.strftime("%d/%m/%y %H:%M:%S %p") #la p es para decir si es am o pm
nowformat7=now.strftime("(%W) (%U) %d/%m/%y %H:%M:%S %p") #W y U son las semanas al año pero con w la semana empieza en domingo y con U en lunes
nowformat8=now.strftime("%c") #formato local del ordenador
nowformat9=now.strftime("%x")
nowformat10=now.strftime("%X")

print(nowformat1,nowformat2,nowformat3,nowformat4,nowformat5,nowformat6,nowformat7,
      nowformat8,nowformat9,nowformat10,sep="\n")

cad="03-05-25 14:30"
fecha=datetime.strptime(cad,"%d-%m-%y %H:%M")
print(fecha)
print(fecha.hour,fecha.year,sep="\n")

if vacaciones>now:
    print("aun falta")
else:
    print("ya fueron")

nuevafecha= ahora+timedelta(hours=8,minutes=30,days=1)
print(ahora,nuevafecha,sep="\n")