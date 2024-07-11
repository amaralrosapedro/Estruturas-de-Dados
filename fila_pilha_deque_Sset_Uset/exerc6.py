

from EstruturasSimplificadas import *

def exerc6():
    # Ler uma linha por vez. Então imprimir todas as linhas ordenadas por
    # tamanho, com a linha mais curta em primeiro. No caso em que duas linhas
    # tenham o mesmo tamanho, resolva sua ordem usando a regra de ordenação alfabética.
    # Linhas duplicadas devem ser impressas apenas uma vez.

    try:
        arq = open("in6.txt", "r")
    except:
        print("Erro ao abrir arquivo de entrada.")
        return

    # Escreva aqui sua resposta para o exercício 6. Não esqueça de usar a função strip()
    # para remover os espaços em branco no início e no fim da string.
    # ATENÇÃO: não use a função readlines() para ler o arquivo de entrada.
    # Sua saída deve ser escrita usando a função print().
    # Você deve usar a estrutura simplificada Pilha, Fila, Deque, SSet, USet ou FilaPrioridade

    fila_aux = FilaPrioridade()
    fila = FilaPrioridade()

    for linha in arq:
      final = linha.strip()
      fila_aux.add(final)

    final_aux = fila_aux.remove()
    fila.add(final_aux)
    while not fila_aux.is_empty():
        final = fila_aux.remove()
        if final != final_aux:
            fila.add(final)
            final_aux = final


    while not fila.is_empty():
        print(fila.remove())


if __name__ == "__main__":
    exerc6()