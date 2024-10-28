from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import faz_jogada
from funcoes import posiciona_frota
from funcoes import afundados
from funcoes import posicao_valida

navios = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']

tamanhos = {'porta-aviões': 4, 'navio-tanque': 3, 'contratorpedeiro': 2, 'submarino': 1}
quantidades = {'porta-aviões': 1, 'navio-tanque': 2, 'contratorpedeiro': 3, 'submarino': 4}

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

for navio in navios:
    tamanho = tamanhos[navio]
    quantidade = 0

    while quantidade < quantidades[navio]:
        
        while True: 
            print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if navio != 'submarino':
                orientacao = int(input('[1] Vertical [2] Horizontal > '))
                orientacao = 'vertical' if orientacao == 1 else 'horizontal'
            else:
                orientacao = None

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)
                quantidade += 1
                break  
            else:
                print('Esta posição não está válida!')  

print(frota)