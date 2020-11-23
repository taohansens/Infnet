"""
Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo amarelo de 100 px de
diâmetro no centro da tela que se move sempre em velocidade permanente na direção que o usuário indicar através das
teclas. Similar ao item anterior, sempre que chegar em uma extremidade, o círculo deve voltar à extremidade oposta e
continuar o com a última direção que o usuário indicou. (código e printscreen)
#Gif em ./Q12 (circulo_mov_loop_tela).gif
"""
import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

clock = pygame.time.Clock()

# Lista de cores
branco = (255, 255, 255)
amarelo = (241, 196, 15)


# Função para desenhar círculo amarelo
def desenha_circulo_amarelo(x, y):
    tela.fill(branco)
    pygame.draw.circle(tela, amarelo, (x, y), 50)


# Controle do limite da tela
def controle_tela():
    if posicao_atual[0] > largura_tela:
        posicao_atual[0] = 0
    if posicao_atual[0] < 0:
        posicao_atual[0] = largura_tela
    if posicao_atual[1] > altura_tela:
        posicao_atual[1] = 0
    if posicao_atual[1] < 0:
        posicao_atual[1] = altura_tela


terminou = False
posicao_atual = [largura_tela/2, altura_tela/2]
desenha_circulo_amarelo(*posicao_atual)

# Inicia variáveis do controle de movimento.
move_baixo = False
move_cima = False
move_esquerda = False
move_direita = False

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
                move_baixo = True
                move_cima = False
                move_esquerda = False
                move_direita = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                move_baixo = False
                move_cima = True
                move_esquerda = False
                move_direita = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_baixo = False
                move_cima = False
                move_esquerda = False
                move_direita = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_baixo = False
                move_cima = False
                move_esquerda = True
                move_direita = False

    # Executa os movimentos em loop
    if move_baixo:
        posicao_atual[1] += 20
    if move_cima:
        posicao_atual[1] -= 20
    if move_direita:
        posicao_atual[0] += 20
    if move_esquerda:
        posicao_atual[0] -= 20

    # Controle do limite da tela, reaparecer na extremidade contrária.
    controle_tela()
    desenha_circulo_amarelo(*posicao_atual)
    # Setando o clock
    clock.tick(30)

# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
