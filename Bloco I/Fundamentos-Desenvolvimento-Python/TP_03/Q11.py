"""
Q.11. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de
diâmetro no centro da tela que se move da esquerda para a direita. Sempre que chegar na extremidade direita, o círculo
deve voltar à extremidade esquerda, retomando o movimento da esquerda para a direita. (código e printscreen)
## Animação armazenada em ./Q11 (circulo_mov_tela).gif
"""

import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

# Lista de cores
branco = (255, 255, 255)
azul = (0, 0, 200)


# Função para desenhar círculo azuç com  50px de raio.
def desenha_circulo_azul(x, y):
    tela.fill(branco)
    pygame.draw.circle(tela, azul, (x, y), 50)


terminou = False
posicao_atual = [largura_tela/2, altura_tela/2]
desenha_circulo_azul(*posicao_atual)

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
                posicao_atual[1] += 20
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                posicao_atual[1] -= 20
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                posicao_atual[0] += 20
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                posicao_atual[0] -= 20

        # Controle do limite da tela, reaparecer na extremidade contrária.
        if posicao_atual[0] > largura_tela:
            posicao_atual[0] = 0
        if posicao_atual[0] < 0:
            posicao_atual[0] = largura_tela
        if posicao_atual[1] > altura_tela:
            posicao_atual[1] = 0
        if posicao_atual[1] < 0:
            posicao_atual[1] = altura_tela
        desenha_circulo_azul(*posicao_atual)

# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
