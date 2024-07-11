

from EstruturasSimplificadas import *
from random import randint

def exerc11():
    # Suponha que você tenha uma Pilha, s, que suporta somente as operações
    # push(x) e pop(). Mostre como, usando somente uma fila FIFO, f, você
    # pode reverter a ordem de todos os elementos em s.

    pilha = Pilha()
    fila = Fila()

    #montando uma pilha S de tamanho aleatorio
    for i in range (0,randint(0, 100)):
      pilha.push(i)

    #coloca a pilha em uma fila
    while pilha.size() != 0:
        fila.add(pilha.pop())

    #inverte a pilha
    while fila.size() != 0:
        pilha.push(fila.remove())

    #imprime a pilha de tras pra frente, logo se a impressão estiver em ordem crescente
    #significa que a pilha esta ao contrario da forma inicial
    while pilha.size():
      print("PILHA AO CONTRARIO")
      print(pilha.pop())



if __name__ == "__main__":
    exerc11()