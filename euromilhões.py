#Estrelas // ainda falta a parte dos 5 numeros
from random import randrange

if __name__ == '__main__':
    x = 0
    lista = [randrange(1, 12), randrange(1, 12)]

while x < len(lista):
    if lista[1] != lista[0]:
        x = x + 1
    if lista[1] == lista[0]:
        lista[1] = randrange(1,12)

    print(f'E1={lista[0]} E2={lista[1]}')
