

from EstruturasSimplificadas import *

def exerc10(string):
    # Uma string casada é uma sequência de caracteres {, }, (, ), [, e ] que
    # estejam casados corretamente. Por exemplo, {{()[]}} é uma string
    # casada, porém {{()]} não é, pois o segundo { casa com um ]. Mostre
    # que uma pilha pode ser usada para isso de tal modo que dada uma string
    # de tamanho n, você possa determinar se ela é uma string casada no tempo O(n).

    # Escreva aqui sua resposta para o exercício 10. Sua resposta deve retornar
    # True ou False de acordo com o resultado do casamento da string.

    pilha = Pilha()
    for item in string:
      if item in "{[(":
          pilha.push(item)
      if item in "}])":
        try:
          teste = pilha.pop()
          if (item == '}' and teste != '{') or (item == ')' and teste != '(') or (item == ']' and teste != '['):
            print("FALSE")
            return
        except:
          print("FALSE")
          return
    if pilha.vazia():
        print("TRUE")
    else:
        print("FALSE")



if __name__ == "__main__":
    exerc10("{{()[]}") # Não é uma string casada
    exerc10("{{()[]}}") # É uma string casada
    exerc10("{{()]}") # Não é uma string casada
    exerc10("{{()[]}}{") # Não é uma string casada
    exerc10("{{()[]}}{}") # É uma string casada
    exerc10("{{()[]}}{}{") # Não é uma string casada
    exerc10("{{()[]}}{}{}") # É uma string casada
    exerc10("{{()[]}}{}{}{") # Não é uma string casada
    exerc10("{{()[]}}{}{}{}") # É uma string casada
    exerc10("{{()[]}}{}{}{}{") # Não é uma string casada
    exerc10("") # É uma string casada