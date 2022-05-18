#Simple exercice that add all 5 random numbers, and find the biggest and smallest number of that 5 random numbers
from random import randrange

if __name__ == '__main__':
    x = 50
    lista = [randrange(x), randrange(x), randrange(x), randrange(x), randrange(x)]
    x = 0
    soma = 0
    menor = lista[0]
    maior = lista[0]

while x < len(lista):
    print(lista[x])
    soma = soma + lista[x]
    if lista[x] < menor:
        menor = lista[x]
    if lista[x] > maior:
        maior = lista[x]
    x = x + 1

    print('Soma', soma, 'Maior', maior, 'Menor', menor)
