def pinSecreto(num):
    digitos=list(str(num).zfill(4))
    resultado=[]
    for n in range(len(digitos)):
        texto="X"*(10-int(digitos[n]))
        texto+="O"*int(digitos[n])
        resultado.append(texto)
    return tuple(resultado)

print("\n".join(pinSecreto(6240)))