"""
Q10. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado no centro da tela.
O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado. (código e printscreen)
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

desenha_quadrado_vermelho(largura_tela/2 - 50, altura_tela/2 - 50)

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
                print("Move Baixo")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print("Move Cima")
            if event.type == pygame.KEYDOWN or event.key == pygame.K_d:
                if event.key == pygame.K_RIGHT:
                    print("Move Direita")
            if event.type == pygame.KEYDOWN or event.key == pygame.K_a:
                if event.key == pygame.K_LEFT:
                    print("Move Esquerda")

# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
