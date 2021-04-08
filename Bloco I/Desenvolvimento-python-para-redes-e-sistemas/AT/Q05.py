def transforma_arquivos(arquivo1, arquivo2):
    textfile1 = open(arquivo1, "r", encoding="utf-8")
    numeros1 = textfile1.read().split(' ')
    textfile2 = open(arquivo2, "r", encoding="utf-8")
    numeros2 = textfile2.read().split(' ')
    if len(numeros1) < len(numeros2):
        qtd = len(numeros2) - len(numeros1)
        for i in range(qtd):
            numeros1.append(0)
    if len(numeros2) < len(numeros1):
        qtd = len(numeros1) - len(numeros2)
        for i in range(qtd):
            numeros2.append(0)
    return numeros1, numeros2


def main():
    file_one = "q05a.txt"
    file_two = "q05b.txt"
    lista = transforma_arquivos(file_one, file_two)
    soma = [int(lista[0][i]) + int(lista[1][i]) for i in range(len(lista[0]))]
    print(soma)


if __name__ == "__main__":
    main()
