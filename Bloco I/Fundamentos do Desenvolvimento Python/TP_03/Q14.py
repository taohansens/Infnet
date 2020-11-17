"""
Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado de tamanho 50 no centro
da tela. Quando o usuário clicar em alguma área da janela, o quadrado deve se mover para a posição clicada.
(código e printscreen)
"""
import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

# Lista de cores
branco = (255, 255, 255)
vermelho = (200, 0, 0)


# Função para desenhar quadrado vermelhor com lado 100px.
def desenha_quadrado_vermelho(x, y):
    tela.fill(branco)
    area = pygame.Rect(x, y, 100, 100)
    pygame.draw.rect(tela, vermelho, area)


terminou = False
posicao_atual = [largura_tela/2 - 50, altura_tela/2 - 50]
desenha_quadrado_vermelho(*posicao_atual)

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
            # Alinha ao centro do quadrado
            posicao_atual = (pos1 - 50, pos2 - 50)

        desenha_quadrado_vermelho(*posicao_atual)
# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
