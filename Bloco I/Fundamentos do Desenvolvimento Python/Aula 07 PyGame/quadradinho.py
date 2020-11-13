import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

terminou = False
while not terminou:
    # atualiza a tela
    pygame.display.update()
    # checar eventods do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()