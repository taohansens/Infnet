"""
PONG:
Q.17 Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” (visto no curso), com uma modificação.
Tal modificação consiste em incluir o aumento da velocidade da bola. O aumento será feito de maneira gradual, isto é, cada 10 vezes que a bola bater na paleta do jogador1 a velocidade aumenta em 1. (código e printscreen)
[x] + várias modificações.
"""

import pygame, sys
from pygame.locals import *

# Provável Menu
# SE jogador == 0, será bot x bot.
# SE jogador == 1, será player x bot.
# SE jogador == 2, player x player.
JOGADOR = 0

# CONSTANTES

# DISPLAY
LARGURA_TELA = 800
ALTURA_TELA = 600

# GAME
LARGURA_LINHA = 10
PALETA_TAMANHO = 50
PALETAOFFSET = 20

# CORES
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)


# Função para desenhar o fundo do jogo
def desenha_arena():
    DISPLAYSURF.fill(PRETO)
    # Desenha a quadra
    pygame.draw.rect(DISPLAYSURF, BRANCO, ((0, 0), (LARGURA_TELA, ALTURA_TELA)), LARGURA_LINHA * 2)
    # Desenha a linha no centro
    pygame.draw.line(DISPLAYSURF, BRANCO, ((LARGURA_TELA // 2), 0), ((LARGURA_TELA // 2), ALTURA_TELA),
                     (LARGURA_LINHA // 4))


# Função para desenhar a paleta
def desenha_paleta(paleta):
    # Impede da paleta ir além da borda do fundo
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA:
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    # Impede da paleta ir além da borda do topo
    elif paleta.top < LARGURA_LINHA:
        paleta.top = LARGURA_LINHA
    # Desenha a paleta
    pygame.draw.rect(DISPLAYSURF, BRANCO, paleta)


# Função para desenhar a bola
def desenha_bola(bola):
    pygame.draw.rect(DISPLAYSURF, BRANCO, bola)


# Função para atualizar posição da bola de acordo com a velocidade
def movimento_bola(bola, eixo_x, eixo_y, acelerador):
    bola.x += eixo_x + acelerador[0]
    bola.y += eixo_y + acelerador[1]
    return bola


# Função para parar de aumentar a velocidade de acordo com o max.
def controle_velocidade(velocidade):
    velocidade_maxima = 8
    if velocidade <= velocidade_maxima:
        velocidade += 1
    else:
        velocidade = 8


# Verifica por colisão com as bordas
# Retorna uma nova posição caso exista colisão
def verifica_colisao(bola, bolaDirX, bolaDirY, acelerador):
    vel_x = acelerador[0]
    vel_y = acelerador[1]
    # Colisão no lado esquerdo
    if bola.left <= (LARGURA_LINHA):
        bola.x = LARGURA_LINHA + (vel_x * -1)
        bolaDirX = bolaDirX * -1

    # Colisão no lado direito
    elif bola.right >= (LARGURA_TELA - LARGURA_LINHA):
        bola.x = (LARGURA_TELA - (LARGURA_LINHA * 2)) - vel_x
        bolaDirX = bolaDirX * -1

    # Colisão na linha superior
    if bola.y <= (LARGURA_LINHA):
        bola.y = LARGURA_LINHA + (vel_y * -1)
        bolaDirY = bolaDirY * -1

    # Colisão na linha inferior
    elif bola.bottom >= (ALTURA_TELA - LARGURA_LINHA):
        bola.y = (ALTURA_TELA - (LARGURA_LINHA * 2)) - vel_y
        bolaDirY = bolaDirY * -1

    return bolaDirX, bolaDirY


# Verifica a colisão da bola com a paleta1 ou paleta2
def verifica_colisao_paletas(bola, paleta1, paleta2, bolaDirX):
    if bolaDirX <= -1 and bola.left <= paleta1.right and bola.top >= paleta1.top and bola.bottom <= paleta1.bottom:
        return bolaDirX * -1
    elif bolaDirX >= 1 and bola.right >= paleta2.left and bola.top >= paleta2.top and bola.bottom <= paleta2.bottom:
        return bolaDirX * -1
    else:
        return bolaDirX


def paleta_bot(bola, bolaDirX, paleta2):
    # Movimentar a paleta quando a bola vem em direção da paleta
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -= 1
    return paleta2


def paleta_double_bot(bola, bolaDirX, paleta1, paleta2, velocidade):
    # Movimentar a paleta quando a bola vem em direção da paleta
    if bolaDirX == 1:
        if paleta2.centery <= bola.centery:
            paleta2.y += 1 * velocidade
        else:
            paleta2.y -= 1 * velocidade
    if bolaDirX == -1:
        if paleta1.centery <= bola.centery:
            paleta1.y += 1 * velocidade
        else:
            paleta1.y -= 1 * velocidade
    return paleta1, paleta2


# Verifica se um jogador fez ponto e retorna o novo valor do placar
def verifica_placar(paleta1, paleta2, bola, placar_left, placar_right, bolaDirX):
    if JOGADOR == 1:
        if bola.left == LARGURA_LINHA:
            return 0
        elif bolaDirX == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
            placar_left += 1
            return placar_left
        elif bola.right == LARGURA_TELA - LARGURA_LINHA:
            placar_left += 10
            return placar_left
        else:
            return placar_left

    if JOGADOR == 0 or JOGADOR == 2:
        # Se a bola passar da paleta esquerda, zera seu placar e soma 10 ao adversario.
        if bola.left == LARGURA_LINHA:
            placar_left = 0
            placar_right += 10
            return placar_left, placar_right

        # Se a bola passar da paleta direita, zera seu placar.
        if bola.right == LARGURA_TELA - LARGURA_LINHA:
            placar_right = 0
            placar_left += 10
            return placar_left, placar_right

        # Se a bola encostar na paleta do lado esquerdo, soma +1 ponto.
        elif bolaDirX == 1 and paleta1.right == bola.left and paleta1.top <= bola.top and paleta1.bottom >= bola.bottom:
            placar_left += 1
            return placar_left, placar_right

        # Se a bola encostar na paleta do lado direito, soma +1 ponto.
        elif bolaDirX == -1 and paleta2.left == bola.right and paleta2.top <= bola.top and paleta2.bottom >= bola.bottom:
            placar_right += 1
            return placar_left, placar_right

        # Bola no meio da partida.
        else:
            return placar_left, placar_right


# Desenha o placar na tela
def desenha_placar(placar_left, placar_right):
    if JOGADOR == 1:
        resultadoSurf = BASICFONT.render('{}'.format(placar_left), True, BRANCO)
        resultadoRect = resultadoSurf.get_rect()
        resultadoRect.topleft = (LARGURA_TELA - 480, 25)
        DISPLAYSURF.blit(resultadoSurf, resultadoRect)
    if JOGADOR == 0 or JOGADOR == 2:
        resultadoSurf1 = BASICFONT.render('{}'.format(placar_left), True, BRANCO)
        resultadoSurf2 = BASICFONT.render('{}'.format(placar_right), True, BRANCO)
        resultadoRect1 = resultadoSurf1.get_rect()
        resultadoRect2 = resultadoSurf2.get_rect()
        resultadoRect1.topleft = (LARGURA_TELA - 480, 25)
        resultadoRect2.topleft = (LARGURA_TELA - 380, 25)
        DISPLAYSURF.blit(resultadoSurf1, resultadoRect1)
        DISPLAYSURF.blit(resultadoSurf2, resultadoRect2)


def main():
    pygame.init()
    # FPS
    FPS = 120
    global DISPLAYSURF
    # Informações sobre a fonte do placar
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 48
    BASICFONT = pygame.font.SysFont('unispacebold', BASICFONTSIZE)
    # Clock
    FPSCLOCK = pygame.time.Clock()
    # Display
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Pong")

    # Posições iniciais
    bolaX = LARGURA_TELA // 2 - LARGURA_LINHA // 2
    bolaY = ALTURA_TELA // 2 - LARGURA_LINHA // 2
    jogadorUm_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2
    jogadorDois_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2

    # Placar
    placar_left = 0
    placar_right = 0

    # Altera posição da bola
    bolaDirX = -1
    bolaDirY = -1

    # Criando os retangulos para a bola e paletas.
    paleta1 = pygame.Rect(PALETAOFFSET, jogadorUm_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA,
                          PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)

    # Desenhando as posições iniciais da arena
    desenha_arena()
    desenha_paleta(paleta1)
    desenha_paleta(paleta2)
    desenha_bola(bola)

    placar_anterior = 0

    acelerador = [0, 0]
    velocidade = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # encerrando janela e finalizando o pygame
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif JOGADOR == 1 or JOGADOR == 2:
                if event.type == MOUSEMOTION:
                    mouseX, mouseY = event.pos
                    # Se apenas um jogador, controlará a paleta esquerda;
                    if JOGADOR == 1:
                        paleta1.y = mouseY
                    # Controlar as duas paletas, a depender da posição do mouse na mesa.
                    # Se estiver mais para esquerda, controlará a paleta esquerda, se não, a paleta direita.
                    if JOGADOR == 2:
                        if mouseX < LARGURA_TELA / 2:
                            paleta1.y = mouseY
                        if mouseX > LARGURA_TELA / 2:
                            paleta2.y = mouseY

        desenha_arena()
        desenha_paleta(paleta1)
        desenha_paleta(paleta2)
        desenha_bola(bola)

        bola = movimento_bola(bola, bolaDirX, bolaDirY, acelerador)

        bolaDirX, bolaDirY = verifica_colisao(bola, bolaDirX, bolaDirY, acelerador)
        bolaDirX = bolaDirX * verifica_colisao_paletas(bola, paleta1, paleta2, bolaDirX)

        if JOGADOR == 0:
            paleta1, paleta2 = paleta_double_bot(bola, bolaDirX, paleta1, paleta2, velocidade)
        if JOGADOR == 1:
            paleta2 = paleta_bot(bola, bolaDirX, paleta2)

        # Retorna placar dependendo da quantidade de jogadores
        if JOGADOR == 1:
            placar_left = verifica_placar(paleta1, paleta2, bola, placar_left, placar_right, bolaDirX)
        else:
            placar_left, placar_right = verifica_placar(paleta1, paleta2, bola, placar_left, placar_right, bolaDirX)

        desenha_placar(placar_left, placar_right)

        if bolaDirX > 0:
            acelerador[0] = velocidade * 1
        else:
            acelerador[0] = velocidade * -1
        if bolaDirY > 0:
            acelerador[1] = velocidade * 1
        else:
            acelerador[1] = velocidade * -1

        # Aumentar 1 na velocidade, a cada 10 pontos do jogador da esquerda.
        multiplo_10 = placar_left % 2 == 0
        placar_atual = placar_left
        if multiplo_10 and placar_atual != placar_anterior:
            placar_anterior = placar_left
            controle_velocidade(velocidade)
            placar_atual = placar_left

        print(velocidade)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
