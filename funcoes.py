
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
def preenche_frota (frota,nome,linha,coluna,orientacao,tamanho):
    i = 0
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome not in frota:
        posicoes = []
        frota[nome] = posicoes
        if orientacao == 'vertical':
            lista = []

            while i < tamanho:
                lista.append([(linha+i),coluna])
                i += 1
            posicoes.append(lista)
        else:
            lista = []
            while i < tamanho:
                lista.append([linha,(coluna+i)])
                i += 1
            posicoes.append(lista)
    else:
        if orientacao == 'vertical':
            lista = []
            while i < tamanho:
                lista.append([(linha+i),coluna])
                i += 1
            frota[nome].append(lista)
        else:
            lista = []
            while i < tamanho:
                lista.append([linha,(coluna+i)])
                i += 1
                posicoes.append(lista)
            frota[nome].append(lista)
    return frota
