import pygame

# CORES
BRANCO = (255, 255, 255)


class Bola:
    def __init__(self, largura, altura, tela, screen_rect):
        self.tela = tela
        self.largura = largura
        self.altura = altura
        self.surface = pygame.Surface([largura, altura])
        # Traz a área retangular da surface
        self.rect = self.surface.get_rect()
        # Seta o centro da tela
        self.centro = screen_rect.center
        self.surface.fill(BRANCO)
        # Seta a velocidade inicial como "5x"
        self.velocidade = 5