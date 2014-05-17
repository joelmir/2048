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
            para = linha[c] != 0
            position_insert = c if not para else c+1
            for next in range(c+1,4):            
                if linha[c] == linha[next] and linha[c] != 0:
                    linha[c] = linha[c] * 2
                    linha[next] = 0
                    break
                elif linha[next] != 0:
                    linha[position_insert], linha[next] = linha[next],0
                    if para:
                        break

def direita(tabuleiro):
    for linha in tabuleiro:
        for c in range(3,0, -1):
            para = linha[c] != 0
            position_insert = c if not para else c-1
            for next in range(c-1, -1, -1):            
                if linha[c] == linha[next] and linha[c] != 0:
                    linha[c] = linha[c] * 2
                    linha[next] = 0
                    break
                elif linha[next] != 0:
                    linha[position_insert], linha[next] = linha[next],0
                    if para:
                        break

def sobe(tabuleiro):
    for coluna in range(4):
        for linha in range(3):
            para = tabuleiro[linha][coluna] != 0
            position_insert = linha if not para else linha+1    
            for next in range(linha+1,4):            
                if tabuleiro[linha][coluna] == tabuleiro[next][coluna] and tabuleiro[linha][coluna] != 0:
                    tabuleiro[linha][coluna] = tabuleiro[linha][coluna] * 2
                    tabuleiro[next][coluna] = 0
                    break
                elif tabuleiro[next][coluna] != 0:
                    tabuleiro[position_insert][coluna], tabuleiro[next][coluna] = tabuleiro[next][coluna],0
                    if para:
                        break

def desce(tabuleiro):
    for coluna in range(4):
        for linha in range(3,0,-1):
            para = tabuleiro[linha][coluna] != 0
            position_insert = linha if not para else linha-1
            for next in range(linha-1,-1, -1):            
                if tabuleiro[linha][coluna] == tabuleiro[next][coluna] and tabuleiro[linha][coluna] != 0:
                    tabuleiro[linha][coluna] = tabuleiro[linha][coluna] * 2
                    tabuleiro[next][coluna] = 0
                    break
                elif tabuleiro[next][coluna] != 0:
                    tabuleiro[position_insert][coluna], tabuleiro[next][coluna] = tabuleiro[next][coluna],0
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
    

            

    

    
    
