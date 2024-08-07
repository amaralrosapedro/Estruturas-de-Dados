# -*- coding: utf-8 -*-
"""sset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YCLtL56sfYQq2U1m8XeC1EKhp5E2jcMs
"""

# implementação de um conjunto de elementos ordenados por tamanho de linha, caso haja empate,
    # ordenar alfabeticamente
class Sset:
    def __init__(self):
        self.elements = []

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
            self.elements.sort(key=lambda x: (len(x), x))

    def remove(self, element):
        self.elements.remove(element)

    def remove(self):
        return self.elements.pop(0)

    def find(self, element):
        if element in self.elements:
            return element
        return None

    def size(self):
        return len(self.elements)

    def get(self):
        return self.elements

    def __contains__(self, element):
        return element in self.elements

    def __str__(self):
        return str(self.elements)