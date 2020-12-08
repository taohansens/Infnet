"""
Q.11. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de
diâmetro no centro da tela que se move da esquerda para a direita. Sempre que chegar na extremidade direita, o círculo
deve voltar à extremidade esquerda, retomando o movimento da esquerda para a direita. (código e printscreen)
## Animação armazenada em ./Q11 (circulo_mov_tela).gif
"""
import random

import pygame

pygame.init()
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

pygame.font.init()
FONTE = pygame.font.SysFont("segoe-bold", 30)

# Lista de cores
branco = (255, 255, 255)
azul = (9, 132, 227)
VERMELHO = (231, 76, 60)

tela.fill(branco)


# Função para desenhar círculo azuç com  50px de raio.
def desenha_circulo_azul(x, y):
    global texto_rect
    circulo = pygame.draw.circle(tela, azul, (x, y), 50)
    texto = FONTE.render("Clique", True, branco)
    texto_rect = texto.get_rect(center=circulo.center)
    tela.blit(texto, texto_rect)


class Retangulo:
    def __init__(self):
        self.largura = 70
        self.altura = 50
        self.x, self.y = random.randint(0, largura_tela - self.largura), random.randint(0, altura_tela - self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)


def checa_colisao(novo_ret):
    for ret_atual in retangulos:
        if ret_atual is not novo_ret and ret_atual.colliderect(novo_ret):
            retangulos.remove(ret_atual)
            if novo_ret in retangulos:
                retangulos.remove(novo_ret)


retangulos = []

terminou = False
while not terminou:
    pygame.display.update()
    # Terminar programa se Quit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if texto_rect.collidepoint(pos):
                r = Retangulo()
                retangulos.append(r.area)
                checa_colisao(r.area)
                print("{} \n {} - {}".format(r.area, len(retangulos), retangulos))

    if len(retangulos) > 0:
        tela.fill(branco)
        for ret in retangulos:
            pygame.draw.rect(tela, VERMELHO, ret)
    desenha_circulo_azul(largura_tela / 2, 60)
    pygame.display.update()


pygame.display.quit()
pygame.quit()
