"""
Q07. Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de
tamanho 50 (cinquenta), toda vez que a tecla espaço for pressionada ou o botão direito for clicado.
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


# Função para desenhar quadrado amarelo com lado 50px.
def desenha_quadrado_amarelo(posx, posy):
    tela.fill(branco)
    area = pygame.Rect(posx, posy, 50, 50)
    pygame.draw.rect(tela, amarelo, area)


# Função para calcular a posição aleatória
def calcula_posicao(tamanho_quadrado):
    max_largura = random.randint(0, largura_tela-tamanho_quadrado)
    max_altura = random.randint(0, altura_tela-tamanho_quadrado)
    return max_largura, max_altura


terminou = False
tela.fill(branco)

while not terminou:
    # atualiza a tela

    pygame.display.update()
    # Terminar programa se Quit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        # Verificar se o botão direito do mouse foi pressionado (event.button == 3)
        # Verifica se a tecla de espaço foi pressionada (K_SPACE)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 or \
                event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            x, y = calcula_posicao(50)
            desenha_quadrado_amarelo(x, y)

# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
