"""
Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo verde de 100 px de diâmetro
 no centro da tela que se inicie o movimento da esquerda para a direita. Sempre que chegar em alguma extremidade,
 o círculo deve trocar a direção e aumentar a velocidade em 1. (código e printscreen)
"""

import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

clock = pygame.time.Clock()

# Lista de cores
branco = (255, 255, 255)
verde = (39, 174, 96)
preto = (0, 0, 0)

# Raio do circulo = 50. == 100 diâmetro.
raio_circulo = 50


# Função para desenhar círculo amarelo
def desenha_circulo_verde(x, y):
    tela.fill(branco)
    pygame.draw.circle(tela, verde, (x, y), raio_circulo)


terminou = False
posicao_atual = [largura_tela/2, altura_tela/2]
desenha_circulo_verde(*posicao_atual)

# Inicia variáveis do controle de movimento.
move_esquerda = False
move_direita = True
# Inicia com a velocidade inicial de 5px.
velocidade = 5

while not terminou:
    # atualiza a tela
    pygame.display.update()
    # Terminar programa se Quit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    # Executa os movimentos em loop
    if move_direita:
        posicao_atual[0] += velocidade
    if move_esquerda:
        posicao_atual[0] -= velocidade

    # Controle do limite da tela, trocar a direção e aumentar a velocidade;
    # descontando 50 do raio do círculo.
    if posicao_atual[0] > largura_tela - raio_circulo:
        move_esquerda = True
        move_direita = False
        velocidade += 1
    if posicao_atual[0] < raio_circulo:
        move_esquerda = False
        move_direita = True
        velocidade += 1

    desenha_circulo_verde(*posicao_atual)
    # Setando o clock
    clock.tick(30)

# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()