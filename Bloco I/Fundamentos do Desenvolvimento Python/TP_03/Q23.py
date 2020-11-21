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
        pygame.draw.line(win, CINZA, (x, 0), (x, SIZE_TELA), 3)
        # Desenha 3 colunas
        pygame.draw.line(win, CINZA, (0, x), (SIZE_TELA, x), 3)


# Inicializa a matriz com as posições centrais de cada célula.
def inicializa_matriz_pos():
    # Calcula o ponto de centro da célula
    centro_celula = SIZE_TELA // 3 // 2

    # Cria matriz com as posições das células,
    lista_posicoes = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(len(lista_posicoes)):
        for j in range(len(lista_posicoes[i])):
            x = centro_celula * (2 * j + 1)
            print(x)
            y = centro_celula * (2 * i + 1)
            # Adiciona as coordenadas do centro de cada célula e adiciona na sua respectiva pos. da matriz.
            lista_posicoes[i][j] = (x, y, "", True)
            print(lista_posicoes[i], [j])
    return lista_posicoes
