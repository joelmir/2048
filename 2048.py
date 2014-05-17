# -*- coding:utf-8 -*-
import random

tabuleiro = []
for i in range(4):
    tabuleiro.append([])
    for j in range(4):
        tabuleiro[i].append(0)

def generate_number():
    return random.randint(1,2)*2

def position_insert(tabuleiro):
    linhas = [linha for linha in tabuleiro if 0 in linha]
    idx_linha = random.randint(0, len(linhas)-1)
    colunas = [idx for idx, coluna in enumerate(linhas[idx_linha]) if coluna == 0]
    idx_coluna = colunas[random.randint(0,len(colunas)-1)]
    linhas[idx_linha][idx_coluna] = generate_number()

def imprimir(tabuleiro):
    for x in tabuleiro:
        print '{0} | {1} | {2} | {3}'.format(x[0], x[1], x[2], x[3])
    print '\n'

def inicializa(tabuleiro):
    for i in range(2):
        position_insert(tabuleiro)
        imprimir(tabuleiro)

def esquerda(tabuleiro):
    for linha in tabuleiro:
        for c in range(3):
            for next_position in range(c+1,4):            
                if linha[c] == linha[next_position] and linha[c] != 0:
                    linha[c] = linha[c] * 2
                    linha[next_position] = 0
                    break
                elif linha[next_position] != 0:
                    para = linha[c] != 0
                    position_insert = c if not para else c+1
                    if position_insert != next_position:
                        linha[position_insert], linha[next_position] = linha[next_position],0
                    if para:
                        break

def direita(tabuleiro):
    for linha in tabuleiro:
        for c in range(3,0, -1):
            for next_position in range(c-1, -1, -1):            
                if linha[c] == linha[next_position] and linha[c] != 0:
                    linha[c] = linha[c] * 2
                    linha[next_position] = 0
                    break
                elif linha[next_position] != 0:
                    para = linha[c] != 0
                    position_insert = c if not para else c-1
                    if position_insert != next_position:
                        linha[position_insert], linha[next_position] = linha[next_position],0
                    if para:
                        break

def sobe(tabuleiro):
    for coluna in range(4):
        for linha in range(3):
            for next_position in range(linha+1,4):            
                if tabuleiro[linha][coluna] == tabuleiro[next_position][coluna] and tabuleiro[linha][coluna] != 0:
                    tabuleiro[linha][coluna] = tabuleiro[linha][coluna] * 2
                    tabuleiro[next_position][coluna] = 0
                    break
                elif tabuleiro[next_position][coluna] != 0:
                    para = tabuleiro[linha][coluna] != 0
                    position_insert = linha if not para else linha+1    
                    
                    if position_insert != next_position:    
                        tabuleiro[position_insert][coluna], tabuleiro[next_position][coluna] = tabuleiro[next_position][coluna],0
                    if para:
                        break

def desce(tabuleiro):
    for coluna in range(4):
        for linha in range(3,0,-1):
            for next_position in range(linha-1,-1, -1):            
                if tabuleiro[linha][coluna] == tabuleiro[next_position][coluna] and tabuleiro[linha][coluna] != 0:
                    tabuleiro[linha][coluna] = tabuleiro[linha][coluna] * 2
                    tabuleiro[next_position][coluna] = 0
                    break
                elif tabuleiro[next_position][coluna] != 0:
                    para = tabuleiro[linha][coluna] != 0
                    position_insert = linha if not para else linha-1
                    if position_insert != next_position:
                        tabuleiro[position_insert][coluna], tabuleiro[next_position][coluna] = tabuleiro[next_position][coluna],0
                    if para:
                        break

inicializa(tabuleiro)

while True:
    key = raw_input("Digite 'W', 'S', 'A', 'D'")
    
    movimento = {'A':esquerda, 'D':direita, 'W':sobe, 'S':desce}
    if movimento.has_key(key.upper()):
        movimento[key.upper()](tabuleiro)
        position_insert(tabuleiro)        
        imprimir(tabuleiro)
    else:
        print 'Fanfarrão!! tecla errada!'
    

            

    

    
    
