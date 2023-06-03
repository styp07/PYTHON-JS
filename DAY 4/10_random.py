import random as rd

# ----------------------- #

aleatorio = rd.randint(1, 50)
print(aleatorio)

aleatorio2 = round(rd.uniform(1, 5), 1)
print(aleatorio2)

aleatorio3 = rd.random()
print(aleatorio3)

colors = ['red', 'green', 'blue']
aleatorio4 = rd.choice(colors)
print(aleatorio4)

numeros = list(range(5, 50, 5))
rd.shuffle(numeros)
print(numeros)