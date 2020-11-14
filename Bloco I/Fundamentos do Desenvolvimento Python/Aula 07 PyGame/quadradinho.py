import pygame, random
# implementando tupla nomeada
from collections import namedtuple

Cor = namedtuple('Cor', ['r', 'g', 'b'])

# cores
lightBlue = (11, 158, 217)
blue = (3, 44, 166)
darkBlue = (2, 24, 89)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (242, 92, 162)
cores = [lightBlue, blue, darkBlue, white, pink]

pygame.init()
largura_tela = 800
altura_tela = 600
clock = pygame.time.Clock()
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Variavel para contar quantas esperas de 60Hz ou 0,016s
conta_clocks = 0
# conta pontuação
pontos = 0
# variavel para contar qtos segundos faltam
conta_segundos = 11


# classe Quadradinho
class Quadradinho:
    def __init__(self):
        self.largura = 20
        self.altura = 20
        self.x, self.y = gera_pos_aleatoria()
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = gera_cor_aleatoria()

    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)


# Para imprimir o texto com o tempo e a pontuação atual
def mostra_placar(tempo, pts):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo restante: " + str(tempo) + "s | Pontuação: " + str(pts), True, white)
    textpos = text.get_rect(centerx=tela.get_width() // 2)
    tela.blit(text, textpos)


# Cria tupla RGB aleatória
def gera_cor_aleatoria():
    # usando namedTuple
    cor = Cor(r=random.randint(0, 255), g=random.randint(0, 255), b=random.randint(0, 255))
    return cor


# Mostra pontuação final ao encerrar o jogo
def mostra_pontuacao_final(tela, pontos):
    tela.fill(black)  # Limpa tela
    font = pygame.font.Font(None, 36)
    text = font.render("Pontuação final: " + str(pontos) + " pontos", 1, white)
    textpos = text.get_rect(center=(tela.get_width() / 2, tela.get_height() / 2))
    tela.blit(text, textpos)


# Cria posicao aleatoria
def gera_pos_aleatoria():
    return random.randint(0, largura_tela - 20), random.randint(0, altura_tela - 20)


terminou = False
while not terminou:
    # atualiza a tela
    pygame.display.update()
    # checar eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Obtem as coordenadas do mouse na tela
            pos = pygame.mouse.get_pos()
            # Checa se foi clicado em algum quadrado
            for q in lista:
                if q.area.collidepoint(pos):
                    lista.remove(q)
                    if q.cor.r < 100 and q.cor.g < 100 and q.cor.b > 175:
                        pontos += 2
                    else:
                        pontos += 1
        if event.type == pygame.QUIT:
            terminou = True
    conta_clocks += 1

    if conta_clocks == 60:
        if conta_segundos > 0:
            conta_segundos -= 1
            conta_clocks = 0
            tela.fill(black)
            lista = []
            mostra_placar(conta_segundos, pontos)
            # cria 20 quadradinhos a cada segundo
            for quadradinho in range(0, 20):
                q = Quadradinho()
                q.desenha(tela)
                lista.append(q)

        else:
            # fim da partida, mostra pontuação
            mostra_pontuacao_final(tela, pontos)
            # e limpa lista de quadradinhos
            for q in lista:
                lista.remove(q)

    # atualiza o desenho na tela
    pygame.display.update()

    # configura o clock em 50 atualizações.
    clock.tick(60)
# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
