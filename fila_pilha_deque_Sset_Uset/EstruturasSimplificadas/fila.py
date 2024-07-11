# -*- coding: utf-8 -*-
"""fila

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mSd9O0N78wzngbrfA7ETKYhRxmRV2YOZ
"""

class Fila:
    def __init__(self):
        self.fila = []
    def add(self, elemento):
        self.fila.append(elemento)
    def remove(self, i = 0):
        return self.fila.pop(i)

    def size(self):
        return len(self.fila)
    def imprimir(self):
        print(self.fila)