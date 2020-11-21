import sys

import pygame

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

# Fonte
FONTE = pygame.font.SysFont('segoi', 40)
DESENHA_JOGADA = pygame.font.SysFont('segoi', 180)

# Cria variável com placares
# pos[0] = X ; pos[1] = BOLA; pos[2] =
placar = [0, 0, 0]


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


# Função para adicionar +1 no placar de quem ganhar..
def soma_placar(pos, placar):
    if pos == 'x':
        placar[0] += 1
    if pos == 'o':
        placar[1] += 1
    print("GANHOU =", placar)


# Função para checar se houve vitória.
def checa_vitoria(posicoes, placar):
    # Checa as colunas
    for coluna in range(len(posicoes)):
        if (posicoes[0][coluna][2] == posicoes[1][coluna][2] == posicoes[2][coluna][2]) and posicoes[coluna][coluna][2] \
                != "":
            soma_placar(posicoes[0][coluna][2], placar)
            tela_final('"' + posicoes[0][coluna][2].upper()+'"' + " GANHOU!", placar)
            # DEV
            print(posicoes)
            return True

    # Checa as linhas
    for linha in range(len(posicoes)):
        if (posicoes[linha][0][2] == posicoes[linha][1][2] == posicoes[linha][2][2]) and posicoes[linha][0][2] != "":
            soma_placar(posicoes[linha][0][2], placar)
            tela_final('"' + posicoes[linha][0][2].upper() + '"' + " GANHOU!", placar)
            # DEV
            print(posicoes)
            return True

    # Checa as diagonais
    if (posicoes[0][0][2] == posicoes[1][1][2] == posicoes[2][2][2]) and posicoes[0][0][2] != "":
        soma_placar(posicoes[0][0][2], placar)
        tela_final('"' + posicoes[0][0][2].upper() + '"' + " GANHOU!", placar)
        return True
    if (posicoes[0][2][2] == posicoes[1][1][2] == posicoes[2][0][2]) and posicoes[0][2][2] != "":
        soma_placar(posicoes[0][2][2], placar)
        tela_final('"' + posicoes[0][2][2].upper() + '"' + " GANHOU!", placar)
        return True

    # Se não houve vencedor, returna False.
    return False


def checa_empate(posicoes, placar):
    # Verifica se ainda há char vazio na posição [2] da matriz, se sim, jogo ainda não acabou
    for i in range(len(posicoes)):
        for j in range(len(posicoes[i])):
            if posicoes[i][j][2] == "":
                return False
    # Soma + 1 no array placar na posição de empate.
    placar[2] += 1
    tela_final("EMPATE", placar)
    # Todas opções foram preenchidas e o checa_vitoria não identificou vencedor, empate = True.
    return True


def tela_final(mensagem, placar):
    pygame.time.delay(300)
    win.fill(BRANCO)
    texto = FONTE.render(mensagem, True, PRETO)
    vit_x = FONTE.render("X: {}".format(placar[0]), True, PRETO)
    vit_o = FONTE.render("O: {}".format(placar[1]), True, PRETO)
    draw = FONTE.render("EMPATES: {}".format(placar[2]), True, PRETO)
    win.blit(texto, ((SIZE_TELA - texto.get_width()) // 2, (SIZE_TELA - texto.get_height()) // 2 - 100))
    win.blit(vit_x, ((SIZE_TELA) // 2, (SIZE_TELA - texto.get_height()) // 2 + 10))
    win.blit(vit_o, ((SIZE_TELA) // 2, (SIZE_TELA - texto.get_height()) //2 + 40))
    win.blit(draw, ((SIZE_TELA) // 2, (SIZE_TELA - texto.get_height()) //2 + 70 ))

    pygame.display.update()
    pygame.time.delay(1500)


# Função principal
def main():

    # Inicializa uma lista que receberá as variáveis (posx, posy, str(X) ou str(o) para realizar o desenho na tela.
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
                                desenho.append((x, y, "X"))
                                # Seta a vez de bola para falsa, e xis True
                                vez_xis = False
                                vez_bola = True
                                # Adiciona a posição da matriz, o caracter que foi jogado, e marca a célula como JOGADA.
                                posicoes[i][j] = (x, y, 'x', True)

                            # Mesma lógica para a vez "Bola".
                            elif vez_bola:
                                desenho.append((x, y, "O"))
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
            imagem = DESENHA_JOGADA.render('{}'.format(xis_or_bola), True, PRETO)
            win.blit(imagem, (x - imagem.get_width() // 2, y - imagem.get_height() // 2))

        if checa_vitoria(posicoes, placar) or checa_empate(posicoes, placar):
            fim_da_partida = True
            print("FIM DA PARTIDA")
            print(placar)

        pygame.display.update()


while True:
    if __name__ == '__main__':
        main()