
#6 erros neste codigo
import random
from ods.binarysearchtree import BinarySearchTree

class Treap(BinarySearchTree):
    class Node(BinarySearchTree.Node):
        def __init__(self, x):
            super(Treap.Node, self).__init__(x)
            self.p = random.random()
            self.size = 1

        def __str__(self):
            return "[%r,%f]" % (self.x, self.p)

    def __init__(self, iterable=[]):
        super(Treap, self).__init__(iterable)

    def _new_node(self, x):
        u = Treap.Node(x)
        u.size = 1
        return u

    def _size(self, u):
        return u.size if u else 0

    def _update_size(self, u):
        if u:
            u.size = 1 + self._size(u.left) + self._size(u.right)

    def add(self, x):
        u = self._new_node(x)
        if self.add_node(u):
            self.bubble_up(u)
            return True
        return False

    def bubble_up(self, u):
        while u != self.r and u.parent.p > u.p:
            if u.parent.right == u:
                self.rotate_left(u.parent)
            else:
                self.rotate_right(u.parent)
            if u.parent:
                self._update_size(u.parent)  # Modificado
        if u.parent == self.nil:
            self.r = u
        self._update_size(u)  # Modificado

    def remove(self, x):
        u = self._find_last(x)
        if u is not None and u.x == x:
            self.trickle_down(u)
            self.splice(u)
            return True
        return False

    def trickle_down(self, u):
        while u.left is not None or u.right is not None:
            if u.left is None:
                self.rotate_left(u)
            elif u.right is None:
                self.rotate_right(u)
            elif u.left.p < u.right.p:
                self.rotate_right(u)
            else:
                self.rotate_left(u)
            if self.r == u:
                self.r = u.parent
            if u:
                self._update_size(u)  # Modificado

    def _get(self, u, i):
        while u is not None:
            left_size = self._size(u.left)
            if i < left_size:
                u = u.left
            elif i == left_size:
                return u.x
            else:
                u = u.right
                i -= left_size + 1
        return None  # Modificado 2


    def get(self, i):
        return self._get(self.r, i)