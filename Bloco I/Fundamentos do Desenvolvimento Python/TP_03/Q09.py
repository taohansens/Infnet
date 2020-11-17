"""
Q.9 Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela. (código e printscreen)
## PrintScreen armazenado em ./Q09 (circulo_azul).jpg
"""
import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

# Lista de cores
branco = (255, 255, 255)
azul = (0, 0, 200)


# Função para desenhar círculo azul com raio 50px.
def desenha_circulo_azul():
    tela.fill(branco)
    pygame.draw.circle(tela, azul, (largura_tela / 2, altura_tela / 2), 50)


terminou = False
# Chama função desenha circulo.
desenha_circulo_azul()

while not terminou:
    # atualiza a tela
    pygame.display.update()
    # Terminar programa se Quit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True


# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
