import pygame

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
