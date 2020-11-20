"""
Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha na tela um estrela de 5 pontas no
tamanho que preferir. (código e printscreen)
"""
import random

import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

# Lista de cores
branco = (255, 255, 255)
amarelo = (243, 156, 18)


# Função para desenhar círculo azul com raio 50px.
def desenhar_estrela(x, y, tamanho):
    surface01 = pygame.Surface((189*tamanho, 200*tamanho))
    surface01.fill(branco)

    pontos_estrela = [[144, 111], [158, 176], [98, 148], [42, 182], [50, 116], [1, 74], [65, 61], [91, 1], [123, 58], [189, 64]]
    poligono_scale = pontos_estrela.copy()
    for pontos in poligono_scale:
        pontos[0] *= tamanho
        pontos[1] *= tamanho
    pygame.draw.polygon(surface01, amarelo, pontos_estrela)
    # Pontos de estrela obtido dos pontos de vetor em formato de estrela (5 pontas).
    tela.fill(branco)
    tela.blit(surface01, (x - 189*tamanho/2,y))


tela.fill(branco)
pygame.display.update()

terminou = False
while not terminou:
    # Terminar programa se Quit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos1, pos2 = pygame.mouse.get_pos()
            tamanho = random.uniform(0.1, 2)
            desenhar_estrela(pos1, pos2, tamanho)
            pygame.display.update()


# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
