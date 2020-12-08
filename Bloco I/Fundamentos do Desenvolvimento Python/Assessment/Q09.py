"""
Q09. Usando o código anterior, escreva um novo programa que, quando as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas, ele
movimente o círculo com o texto “clique” nas direções corretas. Caso colida com algum retângulo, o retângulo que
participou da colisão deve desaparecer.
## Animação armazenada em ./Q09.gif
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


class Circulo:
    def __init__(self, x, y):
        self.raio = 50
        self.area = pygame.Rect(x, y, self.raio*2, self.raio*2)

    def desenha(self):
        pygame.draw.ellipse(tela, azul, self.area)
        texto = FONTE.render("Clique", True, branco)
        button_text_rect = texto.get_rect(center=self.area.center)
        tela.blit(texto, button_text_rect)


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
posicao_atual = [largura_tela // 2 - 50, 10]
Circulo(*posicao_atual)
while not terminou:
    pygame.display.update()
    botao = Circulo(posicao_atual[0], posicao_atual[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if botao.area.collidepoint(pos):
                r = Retangulo()
                retangulos.append(r.area)
                checa_colisao(r.area)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                posicao_atual[1] += 20
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                posicao_atual[1] -= 20
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                posicao_atual[0] += 20
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                posicao_atual[0] -= 20

    if len(retangulos) >= 0:
        tela.fill(branco)
        for ret in retangulos:
            pygame.draw.rect(tela, VERMELHO, ret)
    botao.desenha()

pygame.display.quit()
pygame.quit()
