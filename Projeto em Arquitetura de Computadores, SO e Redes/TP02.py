import pygame
import psutil

# Iniciando a janela principal
largura_tela = 500
altura_tela = 500
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Gerenciador de Recursos")
pygame.display.init()
pygame.font.init()
font = pygame.font.SysFont("segoe-ui", 32)
font2 = pygame.font.SysFont("segoe-ui", 12, "bold")

# Criando 3 surfaces
t1 = pygame.surface.Surface((largura_tela, altura_tela/3))
t2 = pygame.surface.Surface((largura_tela, altura_tela/3))
t3 = pygame.surface.Surface((largura_tela, altura_tela/3))

# Cores
cinza = (236, 240, 241)
escuro = (52, 73, 94)
vermelho = (231, 76, 60)
azul = (52, 152, 219)
branco = (255, 255, 255)


'''pygame.draw.rect(t1, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(t1, (0, 0))

pygame.draw.rect(t3, azul, (20, 50, largura_tela-2*20, 70))
tela.blit(t3, (0, 2*altura_tela/3))
'''


tela.fill(cinza)
t1.fill(cinza)
t2.fill(cinza)


def desenha_barras(secao, variavel, texto, pct):
    tela.blit(secao, (0, 0))
    larg = largura_tela - 2 * 20
    pygame.draw.rect(secao, azul, (40, 50, larg-10, 10))
    larg = larg * variavel / 100
    pygame.draw.rect(secao, vermelho, (40, 50, larg, 10))
    tela.blit(secao, (0, 0))
    texto_barra = texto
    texto_uso = str(pct) + "%"
    text = font.render(texto_barra, 1, escuro)
    uso = font2.render(texto_uso, 1, escuro)
    secao.fill(cinza)
    secao.blit(text, (20, 5))
    secao.blit(uso, (5, 45))

# função de uso da memória
def mostra_uso_memoria():
    tela.blit(t1, (0, 0))
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20
    pygame.draw.rect(t1, azul, (40, 50, larg-10, 10))
    larg = larg*mem.percent/100
    pygame.draw.rect(t1, vermelho, (40, 50, larg, 10))
    tela.blit(t1, (0, 0))
    texto_barra = "Uso de Memória"
    texto_uso = str(mem.percent) + "%"
    text = font.render(texto_barra, 1, escuro)
    uso = font2.render(texto_uso, 1, escuro)
    t1.fill(cinza)
    t1.blit(text, (20, 5))
    t1.blit(uso, (5, 45))


# função de uso do processador
def mostra_uso_cpu():
    tela.blit(t2, (0, altura_tela / 3))
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2*20
    pygame.draw.rect(t2, vermelho, (40, 50, larg-10, 10))
    larg = larg*capacidade/100
    pygame.draw.rect(t2, azul, (40, 50, larg, 10))
    tela.blit(t2, (0, altura_tela / 3))
    texto_barra = "Uso do Processador"
    texto_uso = str(capacidade) + "%"
    text = font.render(texto_barra, 1, escuro)
    uso = font2.render(texto_uso, 1, escuro)
    t2.fill(cinza)
    t2.blit(text, (20, 5))
    t2.blit(uso, (5, 45))



# Cria relógio
clock = pygame.time.Clock()
cont = 60

terminou = False
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    if cont == 60:
        mostra_uso_memoria()
        mostra_uso_cpu()
        cont = 0
    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    clock.tick(60)
    cont += 1

# Finaliza a janela
pygame.display.quit()