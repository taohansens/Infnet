"""
Q.16 Usando a biblioteca Pygame, escreva um programa que desenha na tela estrelas de 5 pontas de tamanhos aleatórios a
cada vez que o usuário clicar na tela. A ponta superior da estrela deve estar situada onde o usuário clicou.
(código e printscreen)
"""

import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

# Lista de cores
branco = (255, 255, 255)
amarelo = (241, 196, 15)


# Função para desenhar quadrado vermelhor com lado 100px.
def desenha_estrela(x, y):
    tela.fill(branco)
    #poligono = [[100, 198], [190, 130], [160, 10], [40, 10], [10, 130]]

    #ok
    poligono = [[40, 10], [100, 198], [160, 10], [10, 130], [190, 130]]

    #poligono = [[y - 100, x - 10], [y - 40, x - 198], [y - 190, x - 78], [y - 10, x - 78], [y - 160, x - 198]]
    pygame.draw.polygon(tela, amarelo, poligono)


terminou = False
posicao_atual = [largura_tela/2, altura_tela/2]
desenha_estrela(*posicao_atual)

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
            posicao_atual = (pos1+224, pos2 + 100)

        desenha_estrela(*posicao_atual)
# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
