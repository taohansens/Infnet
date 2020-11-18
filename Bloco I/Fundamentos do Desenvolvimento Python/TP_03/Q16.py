"""
Q.16 Usando a biblioteca Pygame, escreva um programa que desenha na tela estrelas de 5 pontas de tamanhos aleatórios a
cada vez que o usuário clicar na tela. A ponta superior da estrela deve estar situada onde o usuário clicou.
(código e printscreen)
"""

import pygame
import random

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

# Lista de cores
branco = (255, 255, 255)
amarelo = (241, 196, 15)


# Função para desenhar quadrado vermelhor com lado 100px.
def desenha_estrela(x, y, tamanho):
    tela.fill(branco)
    #poligono = [[100, 198], [40, 10], [190, 130], [10, 130], [160, 10]]
    # tamanho original
    poligono = [[x-100, y-198], [x-40, y-10], [x-190, y-130], [x-10, y-130], [x-160, y-10]]
    # transforma o polígono no tamanho random.
    poligono_scale = poligono.copy()
    for ponto in poligono_scale:
        ponto[0] *= tamanho
        ponto[1] *= tamanho
    pygame.draw.polygon(tela, amarelo, poligono_scale)


terminou = False
posicao_atual = [largura_tela/2, altura_tela/2]
# tamanho inicial
tamanho = 1
desenha_estrela(*posicao_atual, tamanho)

while not terminou:
    # atualiza a tela
    pygame.display.update()
    # Terminar programa se Quit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        # Verificar eventos do mouse;
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos1, pos2 = pygame.mouse.get_pos()
            print("pos mouse: ", pos1,pos2)
            print(posicao_atual)
            # Alinha ao centro do quadrado
            posicao_atual = (pos1, pos2)
            tamanho = random.uniform(0.4, 2)
            print(tamanho)

        desenha_estrela(*posicao_atual, tamanho)
# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
