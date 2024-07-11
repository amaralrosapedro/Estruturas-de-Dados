
from .utils import new_array
from .base import BaseList

class ArrayDeque(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.a = new_array(1)
        self.j = 0
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[(i+self.j)%len(self.a)]

    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[(i+self.j)%len(self.a)]
        self.a[(i+self.j)%len(self.a)] = x
        return y

    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        if i < self.n/2:
            self.j = (self.j-1) % len(self.a)
            for k in range(i):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        else:
            for k in range(self.n, i, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
        self.a[(self.j+i)%len(self.a)] = x
        self.n += 1

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[(self.j+i)%len(self.a)]
        if i < self.n / 2:
            for k in range(i, 0, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
            self.j = (self.j+1) % len(self.a)
        else:
            for k in range(i, self.n-1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        self.n -= 1
        if len(self.a) >= 3*self.n: self._resize()
        return x

    def _resize(self):
        b = new_array(max(1, 2*self.n))
        for k in range(self.n):
            b[k] = self.a[(self.j+k)%len(self.a)]
        self.a = b
        self.j = 0

    def rotate(self, r):
        """Implemente um método rotate(r) que "gire" uma Lista para que o
        item de lista i se torne o item de lista (i + r) mod n. Quando
        executado em um ArrayDeque, rotate(r) deve ser executado
        em tempo O(1 + min{r, n − r}).
        """
        ### Apague o comando pass abaixo e escreva aqui sua solução,
        ### em seguida, execute o teste do diretorio superior
        ### com o comando
        ### python3 test_rotate_lista.py
        n = self.n
        if n == 0:
          return
        r = r % n
        if r < n / 2:
            for i in range(r):
                self.add(0, self.remove(n-1))
        else:
            for i in range(n - r):
                self.add(n-1, self.remove(0))