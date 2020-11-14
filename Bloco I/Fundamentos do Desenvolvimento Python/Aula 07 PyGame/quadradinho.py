import pygame

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
conta_segundos = 0
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
        conta_segundos += 1
        conta_clocks = 0

    tela.fill(darkBlue)

    # Desenha um retângulo não preenchido com linha
    pygame.draw.rect(tela, white, (10, 10, 200, 100), 3)
    # Desenha um retângulo preenchido
    pygame.draw.rect(tela, pink, (400, 300, 50, 50))

    # atualiza o desenho na tela
    pygame.display.update()

    # configura o clock em 50 atualizações.
    clock.tick(60)
# finaliza a janela do jogo
pygame.display.quit()
# finaliza o pygame
pygame.quit()
