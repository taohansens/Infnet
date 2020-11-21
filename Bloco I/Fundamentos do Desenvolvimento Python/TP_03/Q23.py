import sys

import pygame
import math

# Inicializa pyGame
pygame.init()

# Informações tela
SIZE_TELA = 500
win = pygame.display.set_mode((SIZE_TELA, SIZE_TELA))
pygame.display.set_caption("JOGO DA VELHA")

# Lista de cores (R, G, B)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Imagens
X_IMAGE = pygame.transform.scale(pygame.image.load("Images/x.png"), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load("Images/o.png"), (150, 150))

# Fonte
FONTE = pygame.font.SysFont('courier', 40)


def desenha_tabuleiro():
    x = 0
    y = 0
    # Calcula a posição para divisão da tela em 3 pontos.
    distancia = SIZE_TELA // 3
    for i in range(3):
        x = i * distancia
        # Desenha 3 linhas
        pygame.draw.line(win, PRETO, (x, 0), (x, SIZE_TELA), 3)
        # Desenha 3 colunas
        pygame.draw.line(win, PRETO, (0, x), (SIZE_TELA, x), 3)


# Inicializa a matriz com as posições centrais de cada célula.
def matriz_pos():
    # Calcula o ponto de centro da célula
    centro_celula = SIZE_TELA // 3 // 2

    # Cria matriz com as posições das células,
    lista_posicoes = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(len(lista_posicoes)):
        for j in range(len(lista_posicoes[i])):
            x = centro_celula * (2 * j + 1)
            y = centro_celula * (2 * i + 1)
            # Adiciona as coordenadas do centro de cada célula e adiciona na sua respectiva pos. da matriz.
            # Adiciona na posição [3] um boolean para verificar se a célula já foi preenchida ou não.
            lista_posicoes[i][j] = (x, y, "", False)
    return lista_posicoes


# Função principal
def main():

    # Inicializa uma lista que receberá as variáveis (posx, posy, imagemX ou imagemY) para realizar o desenho na tela.
    desenho = []

    # Controle das jogadas, iniciar com "X"
    vez_xis = True
    vez_bola = False

    # Preencher fundo com a cor branca.
    win.fill(BRANCO)

    posicoes = matriz_pos()
    fim_da_partida = False
    while not fim_da_partida:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Captura posição ao clicar
                pos_x, pos_y = pygame.mouse.get_pos()

                for i in range(len(posicoes)):
                    for j in range(len(posicoes)):
                        x, y, char, celula_jogada = posicoes[i][j]
                        # Distancia entre a posição do mouse e o centro do quadrado
                        distancia = ((x - pos_x) ** 2 + (y - pos_y) ** 2) ** 0.5

                        # Se estiver no quadrado, e a célula ainda não tiver sido jogada:
                        if distancia < SIZE_TELA // 3 // 2 and not celula_jogada:
                            # Se for a vez do X:
                            if vez_xis:
                                # Adiciona na lista a posição já calculada do quadrado para desenhar e a imagem do X.
                                desenho.append((x, y, X_IMAGE))
                                # Seta a vez de xis para false
                                vez_xis = False
                                # Adiciona a posição da matriz, o caracter que foi jogado, e marca a célula como JOGADA.
                                posicoes[i][j] = (x, y, 'x', True)
                                # DEV, mostra array da posição marcada
                                print(posicoes)


        # Desenhar o tabuleiro (3x3)
        desenha_tabuleiro()
        pygame.display.update()


while True:
    if __name__ == '__main__':
        main()