while True:
    try:  # intenta
        numtry = int(input("Escribe num: "))
        resultry = 10 / numtry
        # Aquí es lo mismo que con el if, pero en lugar de tirar una exception tira un AssertionError si el numtry es menor que 0
        # assert numtry>=0,"no admito numeros que no son positivos"
        if numtry < 0:
            raise Exception("No entero pos")  # tiramos una excepcion con el mensaje "No entero pos"
    except ZeroDivisionError:  # si das la excepcion ZeroDivisionError haces esto
        print("no se puede divir entre 0")
    except ValueError:  # si das la excepcion ValueErro haces esto
        print("Un valor esta mal")
    except Exception as e:  # Aqui se hace para que agarre la exeption de arriba y muestre su mensaje
        print(e)
    except:  # si das cualquier execepcion no especificada haces esto
        print("error cualquiera")
    else:  # si el try paso sin tirar excepciones haces esto
        print(resultry)
        print("ok")
        break
    finally:  # al terminar siendo bien o mal haces esto
        print("fin")
