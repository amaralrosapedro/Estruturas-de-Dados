

from EstruturasSimplificadas import *

def exerc8(nome_arq = "in8.txt"):
    # Leia toda a entrada uma linha de cada vez e, em seguida, imprimir
    # as linhas pares (começando com a primeira linha, linha 0) seguida pelas linhas ímpares.

    try:
        arq = open(nome_arq, "r")
    except:
        print("Erro ao abrir arquivo de entrada.")
        return

    # Escreva aqui sua resposta para o exercício 8. Não esqueça de usar a função strip()
    # para remover os espaços em branco no início e no fim da string.
    # ATENÇÃO: não use a função readlines() para ler o arquivo de entrada.
    # Sua saída deve ser escrita usando a função print().
    # Você deve usar a estrutura simplificada Pilha, Fila, Deque, SSet, USet ou FilaPrioridade
    par=Fila()
    impar=Fila()
    cont=0
    for linha in arq:
      if cont == 0 or cont % 2 == 0:
        par.add(linha.strip())
        cont+=1
      else:
        impar.add(linha.strip())
        cont+=1
    print("INICIO PAR")
    while not par.size() == 0:
      print(par.remove())
    print("INICIO IMPAR")
    while not impar.size() == 0:
      print(impar.remove())

    # Fim da sua resposta para o exercício 8.

    # fechar arquivo de entrada
    arq.close()

if __name__ == "__main__":
    exerc8()