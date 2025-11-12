def validarMAC(dato):
    LETRAS=["A","B","C","D","E","F"]
    try:
        if str(dato).count(":") > 0 and str(dato).count(".") == 0:
            listaDatos = str(dato).upper().split(":")
            assert len(listaDatos) == 6
            for car in listaDatos:
                if len(car) != 2 and (n for n in car) not in LETRAS and not str(car).isdigit():
                    return False
        elif str(dato).count(".") > 0 and str(dato).count(":") == 0:
            listaDatos = str(dato).upper().split(".")
            assert len(listaDatos) == 3
            for car in listaDatos:
                if len(car) != 4 and (n for n in car) not in LETRAS and not str(car).isdigit():
                    return False

        else:
            raise Exception
    except:
        return False
    return True

def macsValidas(*datos):
    macsValidas=0
    macsNoValidas=0
    for dato in datos:
        valida=validarMAC(dato);

        macsValidas=macsValidas+1 if valida else macsValidas
        macsNoValidas=macsNoValidas+1 if not valida else macsNoValidas
        print(dato, "es valida" if valida else "no es valida")
    print("MACs validas: ",macsValidas)
    print("MACs no validas: ",macsNoValidas)

macsValidas("F48Z","A5B6D7", "F4:8E:38:AF:F4:11","f48e.38af.f41c")