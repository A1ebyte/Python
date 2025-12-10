def cuadrado(x):
    return x**2

print(cuadrado(2))

cuadradoLambda=lambda x: x**2
print(cuadradoLambda(3))

sumaLambda=lambda x,y,z: x+y+z
print(sumaLambda(2,2,4))

parametrosVariosLambda=lambda *x: sum(x)/len(x)
print(parametrosVariosLambda(2,2,4,6,7,8))