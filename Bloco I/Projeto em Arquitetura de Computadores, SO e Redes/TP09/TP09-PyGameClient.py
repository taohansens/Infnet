import pickle
import socket

import pygame
from pygame.locals import *
import sys

# INICIA PYGAME
pygame.init()
CLOCK = pygame.time.Clock()
HZ = 60

# FONTES
pygame.font.init()
FONTE_TITLE = pygame.font.SysFont("segoe-ui-bold", 36)
FONTE_INFO = pygame.font.SysFont("segoe-ui", 18)
FONTE_INFO_BOLD = pygame.font.SysFont("segoe-ui-bold", 26)
FONTE_SUBINFO_BOLD = pygame.font.SysFont("segoe-ui-bold", 20)
FONTE_PERCENT = pygame.font.SysFont("segoe", 26)
FONTE_PERCENT_PROC = pygame.font.SysFont("segoe", 20)

# Iniciando a janela principal
LARGURA_TELA = 600
ALTURA_TELA = 600
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Gerenciador de Recursos | Cliente")

# CORES
CINZA = (236, 240, 241)
ESCURO = (52, 73, 94)
VERMELHO = (231, 76, 60)
AZUL = (52, 152, 219)
BRANCO = (255, 255, 255)

# CONSTANTES COM O TAMANHO DA TELA
TAM_EXIBICAO = (LARGURA_TELA, 100)
TAM_TELA = (LARGURA_TELA, ALTURA_TELA-TAM_EXIBICAO[1])


def get_server(solicitacao):
    # Digite as informações para conexão
    # host = "52.67.6.168"  # Server instanciado na AWS
    host = socket.gethostname()
    porta = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, porta))
        s.send(f"{solicitacao}".encode('ascii'))
        dados = pickle.loads(s.recv(10000))
        s.close()
        informacoes = [dados, (host, porta)]
    except ConnectionRefusedError as error:
        dados = {'conexao': 'ERROR'}
        informacoes = [dados, (host, porta)]
        print(error)
    return informacoes


# Controle de paginação
def navegacao():
    surface = pygame.Surface(TAM_EXIBICAO)
    surface.fill(CINZA)
    seta = pygame.transform.smoothscale(pygame.image.load(r'resources/seta.png')
                                        , (70, 70))
    surface.blit(seta, (340, 10))
    surface.blit(pygame.transform.rotate(seta, 180), (180, 10))
    TELA.blit(surface, (0, ALTURA_TELA - 100))


# Controle de colisão
def colisao_setas(mouse):
    # Posições das setas esquerda e direita
    # Posição no eixo x
    if 510 <= mouse[1] <= 580:
        if 180 <= mouse[0] <= 240:
            return 1
        if 350 <= mouse[0] <= 405:
            return 2


# INÍCIO PÁGINAS ##################
def processador():
    request = get_server("CPU")
    if request[0]['conexao'] == 'ERROR':
        print("Erro na conexão com o servidor")
        raise

    surface = pygame.Surface(TAM_TELA)
    surface.fill(CINZA)

    ALINHAMENTO = 120

    title = FONTE_TITLE.render("INFORMAÇÕES DO PROCESSADOR", True, ESCURO)
    surface.blit(title, (40, 20))

    t_info1 = FONTE_SUBINFO_BOLD.render(f"Processador", True, ESCURO)
    info1 = FONTE_INFO.render(request[0]['name'], True, ESCURO)
    surface.blit(t_info1, (ALINHAMENTO, 60))
    surface.blit(info1, (ALINHAMENTO, 70))

    t_info2 = FONTE_SUBINFO_BOLD.render(f"Sistema", True, ESCURO)
    info2 = FONTE_INFO.render(request[0]['system'], True, ESCURO)
    surface.blit(t_info2, (ALINHAMENTO, 100))
    surface.blit(info2, (ALINHAMENTO, 110))

    t_info3 = FONTE_SUBINFO_BOLD.render(f"Frequência", True, ESCURO)
    info3 = FONTE_INFO.render(f"{request[0]['freq']} MHz", True, ESCURO)
    surface.blit(t_info3, (ALINHAMENTO, 140))
    surface.blit(info3, (ALINHAMENTO, 150))

    t_info4 = FONTE_SUBINFO_BOLD.render(f"Arquitetura", True, ESCURO)
    info4 = FONTE_INFO.render(request[0]['arc'], True, ESCURO)
    surface.blit(t_info4, (ALINHAMENTO + 120, 140))
    surface.blit(info4, (ALINHAMENTO + 120, 150))

    t_info5 = FONTE_SUBINFO_BOLD.render(f"Palavra", True, ESCURO)
    info5 = FONTE_INFO.render(f"{request[0]['word']} bits", True, ESCURO)
    surface.blit(t_info5, (ALINHAMENTO + 240, 140))
    surface.blit(info5, (ALINHAMENTO + 240, 150))

    t_info6 = FONTE_SUBINFO_BOLD.render(f"{request[0]['threads']} threads | {request[0]['cores']} núcleos", True, ESCURO)
    surface.blit(t_info6, (ALINHAMENTO + 80, 180))

    TELA.blit(surface, (0, 0))
# FIM PÁGINAS ##################


def main():
    controle = 60
    pagina = 0
    printed = False  # Variável de controle de impressão no terminal.

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if colisao_setas(pos) == 1:
                    if pagina > 0:
                        pagina -= 1
                if colisao_setas(pos) == 2:
                    if pagina < 12:
                        pagina += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if pagina > 0:
                        pagina -= 1
                if event.key == pygame.K_RIGHT:
                    if pagina < 12:
                        pagina += 1
                if event.key == pygame.K_SPACE:
                    pagina = 11
        if controle == 60:
            navegacao()
            if pagina == 0 and not printed:
                processador()
                printed = True
            controle = 0
        pygame.display.update()
        controle += 1
        CLOCK.tick(HZ)


if __name__ == '__main__':
    main()
