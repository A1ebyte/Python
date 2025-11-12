def divisores(num):
     return {x for x in range(1, num + 1) if num % x == 0}

def divisoresComunes(num1,num2):
    try:
        assert num1>0 and num2>0
        if str(num1).find(".")!=-1 or str(num1).find(".")!=-1:
            raise Exception
    except:
        print("No puedo calcular los divisores comunes de esos números")
        return None

    divisores1 = divisores(num1)
    divisores2 = divisores(num2)

    divisores_comunes = divisores1 & divisores2  # intersección de conjuntos

    if len(divisores_comunes)==1:
        print(f"El unico divisor común de {num1} y {num2} es: 1")
        return 1
    print(f"Los divisores comunes de {num1} y {num2}:",", ".join(str(n) for n in sorted(divisores_comunes)))
    return divisores_comunes

divisoresComunes(22,16)
divisoresComunes(33,17)
divisoresComunes(1725,2500)
divisoresComunes(22.5,1)
divisoresComunes(-1,5)


