"""13. Modifica el programa anterior contemplando que entre los números y las letras
podría haber un espacio en blanco (uno solo) o un guión. En ambos casos se
considerará también que la matrícula es válida (si cumple además lo anterior, claro)"""
matricula = input("Escribe tu matricula:\n").strip().upper()
matriculaLista=[]
valida=True
letrasExcepciones=["A","E","I","O","U","Ñ","Q"]
if matricula.count(" ")==1 and matricula.count("-")==0:
    matriculaLista=matricula.split(" ")
elif matricula.find("-")==1 and matricula.count(" ")==0:
    matriculaLista=matricula.split("-")
matricula="".join(matriculaLista)
if len(matricula)!=7:
    valida=False
if not matricula[0:4].isdigit() or not matricula[4:7].isalpha():
    valida=False
for letra in matricula[4:7]:
    if letrasExcepciones.count(letra)>0:
        valida=False
        break
print("Es valido" if valida==True else "No valido")