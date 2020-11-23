"""
Q10. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado no centro da tela.
O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado. (código e printscreen)
## PrintScreen armazenado em ./Q10 (quadrado_vermelho_mov).jpg após realizar movimentação.
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
        # Verificar eventos do teclado.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                posicao_atual[1] += 5
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                posicao_atual[1] -= 5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                posicao_atual[0] += 5
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                posicao_atual[0] -= 5
        desenha_quadrado_vermelho(*posicao_atual)
# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
