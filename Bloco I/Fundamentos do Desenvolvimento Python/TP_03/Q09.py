"""
Q.9 Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela. (código e printscreen)
"""
import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

clock = pygame.time.Clock()
tela = pygame.display.set_mode((largura_tela, altura_tela))

terminou = False
while not terminou:
    # atualiza a tela
    pygame.display.update()
    # Terminar programa se Quit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    # atualiza o desenho na tela
    pygame.display.update()
    # configura o clock em 60 atualizações.
    clock.tick(60)
    # finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()


