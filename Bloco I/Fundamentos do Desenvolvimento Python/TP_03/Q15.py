"""
Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha na tela um estrela de 5 pontas no
tamanho que preferir. (código e printscreen)
"""
import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

# Lista de cores
branco = (255, 255, 255)
amarelo = (243, 156, 18)


# Função para desenhar círculo azul com raio 50px.
def desenhar_estrela():
    tela.fill(branco)
    # Pontos de estrela obtido dos pontos de vetor em formato de estrela (5 pontas).
    pontos_estrela = [(448, 312), (462, 377), (402, 349), (346, 383), (354, 317), (304, 275), (369, 262), (395, 201), (427, 259), (493, 265)]
    pygame.draw.polygon(tela, amarelo, pontos_estrela)


terminou = False
# Chama função desenha circulo.
desenhar_estrela()


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
