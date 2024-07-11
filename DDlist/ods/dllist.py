
from .base import BaseList

class DLList(BaseList):

    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get_node(self, i):
        if i < self.n/2:
            p = self.dummy.next
            for _ in range(i):
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n, i, -1):
                p = p.prev
        return p

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.get_node(i).x

    def set(self, i, x): #@ReservedAssignment
        if i < 0 or i >= self.n: raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def _remove(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        self._remove(self.get_node(i))

    def add_before(self, w, x):
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i, x):
        if i < 0 or i > self.n:    raise IndexError()
        self.add_before(self.get_node(i), x)

    def __iter__(self):
        u = self.dummy.next
        while u != self.dummy:
            yield u.x
            u = u.next

# Implemente o método rotate(r) que “rotaciona” uma DLList de modo que o
# item i da lista se torne o item (i + r) mod n. Este método deve executar
# em um tempo O(1 + min{r, n − r}) e não deve modificar nenhum nó na lista.
# Você deve completá-lo sem alocar novos nós ou arrays temporários.
# Tudo pode ser feitos apenas manipulando os valores de prev e next dos nós existentes.
    def rotate(self, r):
        if r<=0 or self.n==0 or type(r) != int:
          return
        else:
          r = r % self.n
          elemento_inicio = self.dummy
          tamanho = self.n

          if r <= self.n//2:
            for j in range(r):
              elemento_inicio = elemento_inicio.prev
              antes = elemento_inicio.next.next
              depois = elemento_inicio.prev
              ultimo = elemento_inicio.next
              elemento_inicio.next = antes
              antes.prev.next = elemento_inicio
              elemento_inicio.prev = antes.prev
              antes.prev = elemento_inicio

              ultimo.prev = depois
              depois.next = ultimo
              elemento_inicio = elemento_inicio.prev

          else:
            for i in range (abs(self.n-r)):
              elemento_inicio = elemento_inicio.next
              antes = elemento_inicio.prev.prev
              posto = elemento_inicio.next
              ultimo = elemento_inicio.prev
              elemento_inicio.prev = antes
              antes.next.prev = elemento_inicio
              elemento_inicio.next = antes.next
              antes.next = elemento_inicio

              ultimo.next = posto
              posto.prev = ultimo
              elemento_inicio = elemento_inicio.next