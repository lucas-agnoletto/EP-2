
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

def faz_jogada(tabuleiro, linha, coluna):
    i = linha
    j = coluna

    if tabuleiro[i][j] == 1:
        tabuleiro[i][j] = 'X'

    elif tabuleiro[i][j] == 0:
        tabuleiro[i][j] = '-'

    return tabuleiro
def posiciona_frota(infnavios):
    grid = []
    for tabuleiro in range(0,10):
        tabuleiro = [0]*10
        grid.append(tabuleiro)
    for nome,posições in infnavios.items():
        for posição in posições:
            for posiçaao in posição:
                posy = posiçaao[0]
                posx = posiçaao[1]
                grid[posy][posx] = 1
    return grid
