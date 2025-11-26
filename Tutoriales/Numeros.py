print(5//3) #cociente
print(5%3) #resto/modulo
print(2**2) #elevado

pi=3.141592
print(round(pi,2)) #para rendodear
print(round(pi,3))
print(round(pi,4))

numero = 25
binario = bin(numero) #pasar numero a binario
print(binario)  # Salida: '0b11001'
print(binario[2:]) # Salida: '11001'

binario = "11001"
decimal = int(binario, 2) #el 2 es para decir que es un numerod e base 2
print(decimal)  # 25

print(max(5, 10)) #el maximo
print(min(5, 10, 2)) #el minimo entre los valores
print(abs(-7.25)) #valor absoluto del numero
print(sum([5,5,5,6]))

numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # [2, 4, 6]

int("1") #pasa de string a integer/parseint