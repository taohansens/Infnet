"""
Q.20
Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” alterado na questão anterior e que adicione
 uma nova modificação. Tal modificação consiste em inserir um som (vitória) quando a bola bate na borda atrás da paleta
 do computador. (código)
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


# Função para atualizar posição da bola
def movimento_bola(bola, eixo_x, eixo_y):
    bola.x += eixo_x
    bola.y += eixo_y
    return bola


# Verifica por colisão com as bordas
# Retorna uma nova posição caso exista colisão
def verifica_colisao(bola, bolaDirX, bolaDirY):
    if bola.top == LARGURA_LINHA or bola.bottom == (ALTURA_TELA - LARGURA_LINHA):
        bolaDirY = bolaDirY * -1
    if bola.left == LARGURA_LINHA or bola.right == (LARGURA_TELA - LARGURA_LINHA):
        bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY


# Verifica a colisão da bola com a paleta1 ou paleta2
def verifica_colisao_paletas(bola, paleta1, paleta2, bolaDirX):
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top <= bola.top and paleta1.bottom >= bola.bottom:
        # Se colidir, além de mudar a trajetória, irá execurar o som.
        audio_paleta.play()
        return -1
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top <= bola.top and paleta2.bottom >= bola.bottom:
        # Se colidir, além de mudar a trajetória, irá execurar o som.
        audio_paleta.play()
        return -1
    else:
        return 1


def paleta_bot(bola, bolaDirX, paleta2):
    # Movimentar a paleta quando a bola vem em direção da paleta
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -= 1
    return paleta2


def paleta_double_bot(bola, bolaDirX, paleta1, paleta2):
    # Movimentar a paleta quando a bola vem em direção da paleta
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -= 1
    if bolaDirX == -1:
        if paleta1.centery < bola.centery:
            paleta1.y += 1
        else:
            paleta1.y -= 1
    return paleta1, paleta2


# Verifica se um jogador fez ponto e retorna o novo valor do placar
def verifica_placar(paleta1, paleta2, bola, placar_left, placar_right, bolaDirX, velocidade_aplicada):
    if JOGADOR == 1:
        if bola.left == LARGURA_LINHA:
            return 0
        elif bolaDirX == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
            # Apenas aumentar a pontuação se a velocidade houver sido aumentada 2x.
            if velocidade_aplicada > 0:
                pontuacao = 1 + velocidade_aplicada // 2
                placar_left += pontuacao
            else:
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
            # Apenas aumentar a pontuação se a velocidade houver sido aumentada 2x.
            if velocidade_aplicada > 0:
                pontuacao = 1 + velocidade_aplicada // 2
                placar_left += pontuacao
            else:
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


# Função que executará o áudio da paleta.
def configuracao_som():
    global audio_paleta
    audio_paleta = pygame.mixer.Sound("resources/ball_paletas.wav")
    audio_paleta.set_volume(0.50)


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
    # A cada aumento de velocidade, irá aumentar 50FPS
    velocidade = 50

    # Controle de vezes que aumentou a velocidade para adicionar ao placar esquerdo
    velocidade_vezes = 0

    # Configuração do Som
    configuracao_som()

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

        bola = movimento_bola(bola, bolaDirX, bolaDirY)

        bolaDirX, bolaDirY = verifica_colisao(bola, bolaDirX, bolaDirY)
        bolaDirX = bolaDirX * verifica_colisao_paletas(bola, paleta1, paleta2, bolaDirX)

        if JOGADOR == 0:
            paleta1, paleta2 = paleta_double_bot(bola, bolaDirX, paleta1, paleta2)
        if JOGADOR == 1:
            paleta2 = paleta_bot(bola, bolaDirX, paleta2)

        # Retorna placar dependendo da quantidade de jogadores
        if JOGADOR == 1:
            placar_left = verifica_placar(paleta1, paleta2, bola, placar_left, placar_right, bolaDirX, velocidade_vezes)
        else:
            placar_left, placar_right = verifica_placar(paleta1, paleta2, bola, placar_left, placar_right, bolaDirX,
                                                        velocidade_vezes)

        desenha_placar(placar_left, placar_right)
        multiplo_10 = placar_left % 10 == 0
        placar_atual = placar_left

        # Lógica para aumentar velocidade do jogo
        if multiplo_10 and placar_atual != placar_anterior:
            placar_anterior = placar_left
            FPS += velocidade
            # controle para saber quantas vezes a velocidade foi aumentada.
            velocidade_vezes += 1
            placar_atual = placar_left

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()