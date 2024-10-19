
linha = 2
coluna = 4
orientacao = 'vertical'
tamanho = 3


def define_posicoes(linha, coluna, orientacao, tamanho):
    
    lista_posicoes = [[]]*tamanho
    lista_posicoes[0] = [linha, coluna]

    if orientacao == 'vertical':
        i = 1
        while(i < tamanho):
            lista_posicoes[i] = [linha + i, coluna]
            i += 1

    if orientacao == 'horizontal':
        i = 1
        while(i < tamanho):
            lista_posicoes[i] = [linha, coluna + i]
            i += 1

    return lista_posicoes

print ('2')