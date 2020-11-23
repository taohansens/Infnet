"""
Q.7 Escreva um programa em Python que realiza operações de inclusão e remoção em listas. Seu programa deve perguntar ao usuário qual operação deseja fazer: (código)
- Mostrar lista;
- Incluir elemento;
- Remover elemento;
- Apagar todos os elementos da lista.
Se a opção for a alternativa (a), seu programa deve apenas mostrar o conteúdo da lista. Se a opção for a alternativa (b), seu programa deve pedir o valor do elemento a ser incluído. Se a opção for a alternativa (c), seu programa deve pedir o valor do elemento a ser removido. E se a opção for a alternativa (d), deve-se apenas exibir se a operação foi concluída.
"""

# Inicializa vetor
vetor = ["a","b", 5, 10]


# Função que exibirá o menu
def menu_completo():
    print("=== MENU PRINCIPAL ===")
    print("a) Mostrar lista.")
    print("b) Incluir elemento.")
    print("c) Remover elemento.")
    print("d) Apagar todos os elementos da lista.")
    escolha = input("\nDigite a letra correspondente: ").lower()
    # Se não for escolhida uma das opções corretamente, irá entrar em loop.
    while escolha != 'a' and escolha != 'b' and escolha != 'c' and escolha != 'd':
        print("ESCOLHA INVÁLIDA. DIGITE NOVAMENTE A LETRA CORRESPONDENTE")
        escolha = input("\nDigite a letra correspondente: ").lower()
    # Retornará a escolha realizada.
    return escolha


# posição no vetor adicionada de +1 para exibição.
def mostrar():
    print("== MOSTRANDO LISTA ==")
    print("Elementos encontrados: \n-------------")
    # se houver pelo menos um elemento, faz a iteração.
    if len(vetor) > 0:
        for i in range(0, len(vetor)):
            # percorre vetor e mostra o elemento com sua posição.
            print("Posição {}: {}".format(i+1, vetor[i]))
    else:
        # se não houver elementos na lista.
        print("OPS! Não há elementos na lista.")


# Função para incluir elemento na lista.
def incluir():
    print("== INCLUIR ELEMENTO NA LISTA ==")
    inclusao = input("Digite o elemento que você deseja incluir: ")
    vetor.append(inclusao)
    print("-------------\nSucesso! Elemento ADICIONADO na posição ({})".format(vetor.index(inclusao)+1))


# Função para remover elemento na lista.
def remover():
    print("== REMOVER ELEMENTO NA LISTA ==")
    mostrar()
    print("-------------")
    remove = int(input("Digite a posição do elemento que você deseja remover: "))
    # verifica se é uma posição válida.
    if (remove > 0) and (remove <= len(vetor)):
        # efetua a remoção do elemento da lista.
        vetor.pop(remove-1)
        print("\n#### ELEMENTO REMOVIDO ####\n")
    else:
        print("Erro. Posição não encontrada.")


# Função para limpar lista.
def zerar():
    print("== APAGAR TODOS ELEMENTOS DA LISTA ==")
    print("Você está prestes a apagar toda a lista. TEM CERTEZA?")
    # Verificação.
    apagar_tudo = input("Digite: 'ok' para apagar: ")
    if "ok" in apagar_tudo:
        # Se digitar ok, a lista é apagada.
        vetor.clear()
        print("\n#### OPERAÇÃO CONCLUÍDA ####\n")
    else:
        # Qualquer valor não contendo ok, irá voltar ao menu.
        print("Não entendi. #### Tente novamente.\n")


# executa a função do menu e armazena a opcao escolhida na variável opcao.
# variavel 'terminou' para controle.
terminou = False
# Loop com as funções
while not terminou:
    opcao = menu_completo()
    # opções do menu e a chamada correspondente da função
    if opcao == 'a':
        mostrar()
    if opcao == 'b':
        incluir()
    if opcao == 'c':
        remover()
    if opcao == 'd':
        zerar()

    # controle para encerramento do programa
    escolha = input("-------------\nVoltar ao menu? Qualquer tecla para voltar / 0 - para encerrar.")
    if escolha == '0':
        terminou = True
