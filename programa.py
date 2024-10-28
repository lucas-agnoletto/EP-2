from funcoes import define_posicoes, preenche_frota, faz_jogada
from funcoes import posiciona_frota, afundados, posicao_valida

navios = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
tamanhos = {'porta-aviões': 4, 'navio-tanque': 3, 'contratorpedeiro': 2, 'submarino': 1}
quantidades = {'porta-aviões': 1, 'navio-tanque': 2, 'contratorpedeiro': 3, 'submarino': 4}

frota = {navio: [] for navio in navios}

def solicitar_coordenadas(navio, tamanho):
    print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))

    if navio != 'submarino':
        orientacao = int(input('[1] Vertical [2] Horizontal > '))
        orientacao = 'vertical' if orientacao == 1 else 'horizontal'
    else:
        orientacao = None

    return linha, coluna, orientacao

for navio in navios:
    tamanho = tamanhos[navio]
    quantidade = 0

    while quantidade < quantidades[navio]:
        linha, coluna, orientacao = solicitar_coordenadas(navio, tamanho)

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)
            quantidade += 1  
        else:
            print('Esta posição não está válida!')

print(frota)
