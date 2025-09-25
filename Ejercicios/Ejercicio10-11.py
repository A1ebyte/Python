import random
dado1=0
dado2=-1
tiradas=0
#print(f'1er Dado = {dado1}, 2do Dado = {dado2}')
while dado1 != dado2:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    tiradas+=1
    print(f'{tiradas}. 1er Dado = {dado1}, 2do Dado = {dado2}')
print(f"He tirado: {tiradas} veces los lados hasta ser iguales")