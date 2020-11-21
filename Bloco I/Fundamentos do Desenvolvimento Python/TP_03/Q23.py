import sys

import pygame
import math

# Inicializa pyGame
pygame.init()

# Informações tela
SIZE_TELA = 500
win = pygame.display.set_mode((SIZE_TELA, SIZE_TELA))
pygame.display.set_caption("JOGO DA VELHA")

# Lista de cores (R, G, B)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Imagens
X_IMAGE = pygame.transform.scale(pygame.image.load("Images/x.png"), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load("Images/o.png"), (150, 150))

# Fonte
FONTE = pygame.font.SysFont('courier', 40)


def desenha_tabuleiro():
    x = 0
    y = 0
    # Calcula a posição para divisão da tela em 3 pontos.
    distancia = SIZE_TELA // 3
    for i in range(3):
        x = i * distancia
        # Desenha 3 linhas
        pygame.draw.line(win, PRETO, (x, 0), (x, SIZE_TELA), 3)
        # Desenha 3 colunas
        pygame.draw.line(win, PRETO, (0, x), (SIZE_TELA, x), 3)


# Inicializa a matriz com as posições centrais de cada célula.
def matriz_pos():
    # Calcula o ponto de centro da célula
    centro_celula = SIZE_TELA // 3 // 2

    # Cria matriz com as posições das células,
    lista_posicoes = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(len(lista_posicoes)):
        for j in range(len(lista_posicoes[i])):
            x = centro_celula * (2 * j + 1)
            y = centro_celula * (2 * i + 1)
            # Adiciona as coordenadas do centro de cada célula e adiciona na sua respectiva pos. da matriz.
            # Adiciona na posição [3] um boolean para verificar se a célula já foi preenchida ou não.
            lista_posicoes[i][j] = (x, y, "", False)
    return lista_posicoes


def checa_vitoria(posicoes):
    # Checa as colunas

    for coluna in range(len(posicoes)):
        if (posicoes[0][coluna][2] == posicoes[1][coluna][2] == posicoes[2][coluna][2]) and posicoes[coluna][coluna][2] != "":
            print("vitória na coluna de: ", posicoes[0][coluna][2])
            # DEV
            print(posicoes)
            return True

    # Checa as linhas
    for linha in range(len(posicoes)):
        if (posicoes[linha][0][2] == posicoes[linha][1][2] == posicoes[linha][2][2]) and posicoes[linha][0][2] != "":
            print("vitória na linha de: ", posicoes[linha][0][2])
            # DEV
            print(posicoes)
            return True
    # Checa as diagonais
    if (posicoes[0][0][2] == posicoes[1][1][2] == posicoes[2][2][2]) and posicoes[0][0][2] != "":
        print("vitória na diagonal1 de: ", posicoes[0][0][2])
        return True
    if (posicoes[0][2][2] == posicoes[1][1][2] == posicoes[2][0][2]) and posicoes[0][2][2] != "":
        print("vitória na diagonal2 de: ", posicoes[0][2][2])
        return True

    # Se não houve vencedor, returna False.
    return False


def checa_empate(posicoes):
    # Verifica se ainda há char vazio na posição [2] da matriz, se sim, jogo ainda não acabou
    for i in range(len(posicoes)):
        for j in range(len(posicoes[i])):
            if posicoes[i][j][2] == "":
                return False
    # Todas opções foram preenchidas e o checa_vitoria não identificou vencedor, empate = True.
    print("EMPATE")
    return True


# Função principal
def main():

    # Inicializa uma lista que receberá as variáveis (posx, posy, imagemX ou imagemY) para realizar o desenho na tela.
    desenho = []

    # Controle das jogadas, iniciar com "X"
    vez_xis = True
    vez_bola = False

    # Preencher fundo com a cor branca.
    win.fill(BRANCO)

    posicoes = matriz_pos()
    fim_da_partida = False
    while not fim_da_partida:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Captura posição ao clicar
                pos_x, pos_y = pygame.mouse.get_pos()
                for i in range(len(posicoes)):
                    for j in range(len(posicoes)):
                        x, y, char, celula_jogada = posicoes[i][j]
                        # Distancia entre a posição do mouse e o centro do quadrado
                        distancia = ((x - pos_x) ** 2 + (y - pos_y) ** 2) ** 0.5

                        # Se estiver no quadrado, e a célula ainda não tiver sido jogada:
                        if distancia < SIZE_TELA // 3 // 2 and not celula_jogada:
                            # Se for a vez do X:
                            if vez_xis:
                                # Adiciona na lista a posição já calculada do quadrado para desenhar e a imagem do X.
                                desenho.append((x, y, X_IMAGE))
                                # Seta a vez de bola para falsa, e xis True
                                vez_xis = False
                                vez_bola = True
                                # Adiciona a posição da matriz, o caracter que foi jogado, e marca a célula como JOGADA.
                                posicoes[i][j] = (x, y, 'x', True)

                            # Mesma lógica para a vez "Bola".
                            elif vez_bola:
                                desenho.append((x, y, O_IMAGE))
                                # Seta a vez de bola para falsa, e xis True
                                vez_bola = False
                                vez_xis = True
                                # Adiciona a posição da matriz, o caracter que foi jogado, e marca a célula como JOGADA.
                                posicoes[i][j] = (x, y, 'o', True)


        # Desenhar o tabuleiro (3x3)
        desenha_tabuleiro()

        # Desenhar X ou Bola:
        for jogada in desenho:
            x, y, xis_or_bola = jogada
            win.blit(xis_or_bola, (x - xis_or_bola.get_width() // 2, y - xis_or_bola.get_height() // 2))

        if checa_vitoria(posicoes) or checa_empate(posicoes):
            fim_da_partida = True
            print("FIM DA PARTIDA")

        pygame.display.update()


while True:
    if __name__ == '__main__':
        main()