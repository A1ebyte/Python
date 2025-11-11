import random  #para poder hacer los randoms
print(random.randint(0,2)) #numero random entre 0-2 incluidos
print(random.uniform(20, 60)) #un numero decimal entre 20-60 incluidos

lista=["001","010","011","100","101","110","111"]
print(random.choice(lista))   #elige aleatoriamente de la lista
print(random.sample(lista,2))  #2 elementos random que no se repiten
random.shuffle(lista) #desordena la lista