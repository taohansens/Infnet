import pygame, random

pygame.init()
largura_tela = 800
altura_tela = 600

# cores
lightBlue = (11, 158, 217)
blue = (3, 44, 166)
darkBlue = (2, 24, 89)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (242, 92, 162)
cores = [lightBlue, blue, darkBlue, white, pink]

clock = pygame.time.Clock()
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Variavel para contar quantas esperas de 60Hz ou 0,016s
conta_clocks = 0
# conta quantos quadradinhos clicou
pontos = 0
# variavel para contar qtos segundos passaram
conta_segundos = 5


# Para imprimir o texto com o tempo e a pontuação corrente
def mostra_tempo(tempo, pontos):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s | Pontuação: " + str(pontos), 1, white)
    textpos = text.get_rect(centerx=tela.get_width() // 2)
    tela.blit(text, textpos)


# Cria tupla RGB aleatória
def gera_cor_aleatoria():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# Mostra pontuação final ao encerrar o jogo
def mostra_pontuacao_final(tela, pontos):
    tela.fill(black) # Limpa tela
    font = pygame.font.Font(None, 36)
    text = font.render("Pontuação: " + str(pontos) + " quadradinhos", 1, white)
    textpos = text.get_rect(center=(tela.get_width()/2, tela.get_height()/2))
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
                if q.collidepoint(pos):
                    lista.remove(q)
                    pontos = pontos + 1

        if event.type == pygame.QUIT:
            terminou = True
    conta_clocks += 1
    if conta_clocks == 60:
        if conta_segundos > 0:
            # Mostra tempo restante na tela com a pontuação
            mostra_tempo(conta_segundos, pontos)

            conta_segundos -= 1
            conta_clocks = 0
            tela.fill(black)
            lista = []
            # cria 20 quadradinhos a cada segundo
            for quadradinho in range(0, 20):
                x, y = gera_pos_aleatoria()
                q = pygame.Rect(x, y, 20, 20)
                pygame.draw.rect(tela, gera_cor_aleatoria(), q)
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
