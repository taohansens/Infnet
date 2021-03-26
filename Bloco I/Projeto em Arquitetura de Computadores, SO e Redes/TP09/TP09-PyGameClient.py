import json
import socket

import pygame
from pygame.locals import *
import sys

from psutil._common import bytes2human

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
FONTE_SUBINFO_BOLD_X = pygame.font.SysFont("segoe-ui-bold", 24)
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
    host = socket.gethostname()
    porta = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dados = {'conexao': 'ERROR'}
    try:
        s.connect((host, porta))
        s.send(f"{solicitacao}".encode('ascii'))
        request = b''
        while True:
            data = s.recv(1024)
            request = request + data
            try:
                dados = json.loads(request)
                break
            except:
                continue
        informacoes = [dados, (host, porta)]
    except ConnectionRefusedError as error:
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

    t_info3 = FONTE_SUBINFO_BOLD.render(f"Frequência Atual/Total", True, ESCURO)
    info3 = FONTE_INFO.render(f"{request[0]['freq_atual']} MHz / {request[0]['freq']}MHz", True, ESCURO)
    surface.blit(t_info3, (ALINHAMENTO-80, 140))
    surface.blit(info3, (ALINHAMENTO-95, 150))

    t_info4 = FONTE_SUBINFO_BOLD.render(f"Arquitetura", True, ESCURO)
    info4 = FONTE_INFO.render(request[0]['arc'], True, ESCURO)
    surface.blit(t_info4, (ALINHAMENTO + 120, 140))
    surface.blit(info4, (ALINHAMENTO + 120, 150))

    t_info5 = FONTE_SUBINFO_BOLD.render(f"Palavra", True, ESCURO)
    info5 = FONTE_INFO.render(f"{request[0]['word']} bits", True, ESCURO)
    surface.blit(t_info5, (ALINHAMENTO + 240, 140))
    surface.blit(info5, (ALINHAMENTO + 240, 150))

    t_info6 = FONTE_SUBINFO_BOLD.render(f"{request[0]['threads']} threads | {request[0]['cores']} núcleos", True, ESCURO)
    surface.blit(t_info6, (ALINHAMENTO + 100, 180))

    t_info7 = FONTE_SUBINFO_BOLD.render(f"Uso por CPU", True, ESCURO)
    surface.blit(t_info7, (20, 180))

    convert_cpu = float(request[0]['uso_cpu_todos'])
    t_info8 = FONTE_SUBINFO_BOLD.render("Uso Geral", True, ESCURO)
    t_info9 = FONTE_SUBINFO_BOLD.render(f"{convert_cpu}%", True, ESCURO)
    surface.blit(t_info8, (20, 80))
    surface.blit(t_info9, (10, 105))

    pygame.draw.rect(surface, AZUL, (50, 100, 50, 20))
    pos_final_barra_uso = 50 * (convert_cpu / 100)
    pygame.draw.rect(surface, VERMELHO, [50, 100, pos_final_barra_uso, 20])

    # Exibição por cpu.
    var_barra = 0
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)

    for i in request[0]['uso_cpu']:
        percentagem_uso = FONTE_PERCENT_PROC.render(f"{i}%", True, ESCURO)
        surface.blit(percentagem_uso, (15, 200 + var_barra))
        pygame.draw.rect(surface, AZUL, (60, 200 + var_barra, pos_final_barra, 15))
        pos_final_barra_uso = pos_final_barra * (i / 100)
        pygame.draw.rect(surface, VERMELHO, (60, 200 + var_barra, pos_final_barra_uso, 15))
        var_barra += 25

    TELA.blit(surface, (0, 0))


def memoria_ram_rede():
    request = get_server("MEMORY")
    surface = pygame.Surface(TAM_TELA)
    surface.fill(CINZA)
    ALINHAMENTO = 120
    # Posições em pixels
    pos_altura_barra = 110
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    # Desenha barra total (em azul)
    pygame.draw.rect(surface, AZUL, (70, pos_altura_barra, pos_final_barra, 45))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = pos_final_barra * (request[0]['percent'] / 100)
    pygame.draw.rect(surface, VERMELHO, (70, pos_altura_barra, pos_final_barra_uso, 45))

    title = FONTE_TITLE.render("INFORMAÇÕES MEMÓRIA", True, ESCURO)
    surface.blit(title, (150, 40))

    t_info1 = FONTE_PERCENT.render(f"{request[0]['percent']}%", True, ESCURO)
    surface.blit(t_info1, (20, 125))

    t_info2 = FONTE_SUBINFO_BOLD.render(f"Memória Em Uso", True, ESCURO)
    info2 = FONTE_INFO_BOLD.render(f"{bytes2human(request[0]['used'])}", True, ESCURO)
    surface.blit(t_info2, (ALINHAMENTO, 170))
    surface.blit(info2, (ALINHAMENTO, 185))

    t_info3 = FONTE_SUBINFO_BOLD.render(f"Memória Física Total", True, ESCURO)
    info3 = FONTE_INFO_BOLD.render(f"{bytes2human(request[0]['total'])}", True, ESCURO)
    surface.blit(t_info3, (ALINHAMENTO + 300, 170))
    surface.blit(info3, (ALINHAMENTO + 300, 185))

    t_info4 = FONTE_SUBINFO_BOLD.render(f"Memória Livre", True, ESCURO)
    info4 = FONTE_INFO_BOLD.render(f"{bytes2human(request[0]['free'])}", True, ESCURO)
    surface.blit(t_info4, (ALINHAMENTO + 160, 170))
    surface.blit(info4, (ALINHAMENTO + 160, 185))

    request_rede = get_server("REDE")
    title2 = FONTE_TITLE.render("INFORMAÇÕES REDE", True, ESCURO)
    surface.blit(title2, (150, 300))

    info5 = FONTE_INFO_BOLD.render(f"IPv4", True, ESCURO)
    info5_1 = FONTE_TITLE.render(f"{request_rede[0]['ipv4']}", True, AZUL)
    surface.blit(info5, (150, 340))
    surface.blit(info5_1, (150, 360))

    info6 = FONTE_INFO_BOLD.render(f"Máscara de Rede", True, ESCURO)
    info6_1 = FONTE_TITLE.render(f"{request_rede[0]['net_mask']}", True, AZUL)
    surface.blit(info6, (150, 390))
    surface.blit(info6_1, (150, 410))

    info7 = FONTE_INFO_BOLD.render(f"Gateway", True, ESCURO)
    info7_1 = FONTE_TITLE.render(f"{request_rede[0]['gateway']}", True, AZUL)
    surface.blit(info7, (150, 440))
    surface.blit(info7_1, (150, 460))

    info8 = FONTE_INFO_BOLD.render(f"IP público", True, ESCURO)
    info8_1 = FONTE_TITLE.render(f"{request_rede[0]['public_ip']}", True, AZUL)
    surface.blit(info8, (300, 340))
    surface.blit(info8_1, (300, 360))



    TELA.blit(surface, (0, 0))

def discos():
    request = get_server("DISKS")
    surface = pygame.Surface(TAM_TELA)
    surface.fill(CINZA)

    ALINHAMENTO = 80
    # Posições em pixels
    pos_altura_barra = 110
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    # Desenha barra total (em azul)
    pygame.draw.rect(surface, AZUL, (70, pos_altura_barra, pos_final_barra, 30))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = pos_final_barra * (request[0][5] / 100)
    pygame.draw.rect(surface, VERMELHO, (70, pos_altura_barra, pos_final_barra_uso, 30))

    title = FONTE_TITLE.render("ARMAZENAMENTO TOTAL - DISCO(S)", True, ESCURO)
    surface.blit(title, (80, 40))
    info1 = FONTE_PERCENT.render(f"{request[0][5]}%", True, ESCURO)
    surface.blit(info1, (15, pos_altura_barra + 5))

    t_info2 = FONTE_SUBINFO_BOLD.render(f"QTD DE DISCOS ENCONTRADOS", True, ESCURO)
    info2 = FONTE_INFO_BOLD.render(f"{round(request[0][0])}", True, ESCURO)
    surface.blit(t_info2, (ALINHAMENTO, 185))
    surface.blit(info2, (ALINHAMENTO, 200))

    t_info3 = FONTE_SUBINFO_BOLD.render(f"PONTOS DE MONTAGEM", True, ESCURO)
    info3 = FONTE_INFO_BOLD.render(f"{request[0][1]}", True, ESCURO)
    surface.blit(t_info3, (ALINHAMENTO + 300, 185))
    surface.blit(info3, (ALINHAMENTO + 300, 200))

    t_info4 = FONTE_SUBINFO_BOLD_X.render(f"ESPAÇO TOTAL", True, ESCURO)
    info4 = FONTE_TITLE.render(f"{bytes2human(request[0][2])}", True, ESCURO)
    info4_1 = FONTE_PERCENT_PROC.render(f"({request[0][2]}) BYTES", True, ESCURO)
    surface.blit(t_info4, (ALINHAMENTO, 240))
    surface.blit(info4, (ALINHAMENTO, 265))
    surface.blit(info4_1, (ALINHAMENTO, 290))

    t_info5 = FONTE_SUBINFO_BOLD_X.render(f"ESPAÇO TOTAL UTILIZADO", True, ESCURO)
    info5 = FONTE_TITLE.render(f"{bytes2human(request[0][3])}", True, VERMELHO)
    info5_1 = FONTE_PERCENT_PROC.render(f"({request[0][3]}) BYTES", True, VERMELHO)
    surface.blit(t_info5, (ALINHAMENTO + 130, 330))
    surface.blit(info5, (ALINHAMENTO + 130, 350))
    surface.blit(info5_1, (ALINHAMENTO + 130, 375))

    t_info6 = FONTE_SUBINFO_BOLD_X.render(f"ESPAÇO TOTAL LIVRE", True, ESCURO)
    info6 = FONTE_TITLE.render(f"{bytes2human(request[0][4])}", True, AZUL)
    info6_1 = FONTE_PERCENT_PROC.render(f"({request[0][4]}) BYTES", True, AZUL)
    surface.blit(t_info6, (ALINHAMENTO + 280, 240))
    surface.blit(info6, (ALINHAMENTO + 280, 265))
    surface.blit(info6_1, (ALINHAMENTO + 280, 290))

    TELA.blit(surface, (0, 0))


def arquivos():
    request = get_server("FILES")
    # print_arquivos_terminal(request)
    surface = pygame.Surface(TAM_TELA)
    surface.fill(CINZA)

    # Posições em pixels
    pos_altura_barra = 50

    # Textos Info processador
    # Título
    titulo = FONTE_TITLE.render(f"Listagem de Arquivos", True, ESCURO)
    surface.blit(titulo, (40, 20))

    templ = "%3s %0s %22s %25s %20s"
    header = (templ % ("TIPO", "NOME", "TAMANHO", "DATA MOD", "DATA CRI"))

    header_table = FONTE_SUBINFO_BOLD.render(header, True, ESCURO)
    surface.blit(header_table, (40, pos_altura_barra + 50))

    # impressão de arquivos
    distancia_px = 10
    for d in request[0]:
        templ = "%3s %-20s %-5s %20s %20s"
        distancia_px += 20
        file = templ % (
            request[0][d]['isfile'],
            request[0][d]['arquivo'][:15],
            bytes2human(request[0][d]['tamanho']),
            request[0][d]['atime'],
            request[0][d]['mtime'])
        ls_arquivo = FONTE_INFO.render(file, True, ESCURO)
        surface.blit(ls_arquivo, (40, 90 + distancia_px))

    TELA.blit(surface, (0, 0))


def print_arquivos_terminal(lista):
    print("####### LISTAGEM DE ARQUIVOS | SERVER #######")
    templ = "%3s %0s %22s %10s %20s"
    print(templ % ("TIPO", "NOME", "TAMANHO", "DATA MOD", "DATA CRI"))
    for d in lista[0]:
        templ = "%3s %-20s %-5s %20s %20s"
        print(templ % (
            lista[0][d]['isfile'],
            lista[0][d]['arquivo'][:20],
            bytes2human(lista[0][d]['tamanho']),
            lista[0][d]['atime'],
            lista[0][d]['mtime']))
    print("\n###### FINAL LISTAGEM ARQUIVOS ######")

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
                #processador()
                arquivos()
                printed = True
            if pagina == 1 and printed:
                memoria_ram_rede()
                printed = False
            if pagina == 2 and not printed:
                discos()
                printed = True
            if pagina == 3 and printed:
                arquivos()
                printed = False
            controle = 0
        pygame.display.update()
        controle += 1
        CLOCK.tick(HZ)


if __name__ == '__main__':
    main()
