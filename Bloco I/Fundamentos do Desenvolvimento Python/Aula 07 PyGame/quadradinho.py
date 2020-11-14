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
conta_segundos = 10


# Para imprimir o texto com o tempo e a pontuação corrente
def mostra_tempo(tempo, pontos):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s | Pontuação: " + str(pontos), 1, white)
    textpos = text.get_rect(centerx=tela.get_width() // 2)
    tela.blit(text, textpos)


terminou = False
while not terminou:
    # atualiza a tela
    pygame.display.update()
    # checar eventods do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    conta_clocks += 1
    if conta_clocks == 60:
        if conta_segundos > 0:
            conta_segundos -= 1
            conta_clocks = 0
            tela.fill(cores[random.randint(0, 4)])
        else:
            terminou = True

    mostra_tempo(conta_segundos, pontos)

    # atualiza o desenho na tela
    pygame.display.update()

    # configura o clock em 50 atualizações.
    clock.tick(60)
# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
