import locale

def mostraNaTela(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    dinheiroTotal = locale.currency(valor[0], grouping=True, symbol=None)
    dinheiroPessoa = locale.currency(valor[1], grouping=True, symbol=None)
    txt1 = 'O valor total da conta, com a taxa de serviço, será de R${}.\n'.format(dinheiroTotal)
    txt2 = 'Dividindo a conta por {} pessoa(s), cada uma deverá pagar R${}.'.format(valor[2], dinheiroPessoa)
    txt3 = 'Deverá pagar, sozinho, R${}'.format(dinheiroTotal)
    if valor[2] == 1:
        return print(txt1 + txt3)
    else:
        return print(txt1 + txt2)


def calcularConta(valor, pessoas, servico):
    valorTotal = valor * (1 + servico / 100)
    valorPagar = valorTotal / pessoas
    return valorTotal, valorPagar, pessoas


valorConta = 0
while valorConta <= 0:
    valorConta = float(input("Digite o valor total da conta: R$"))
    if not (valorConta > 0):
        print(ValueError("Esse valor é inválido."))

qtdPessoas = 0
while qtdPessoas <= 0:
    qtdPessoas = int(input("Digite a quantidade de pessoas: "))
    if not (qtdPessoas > 0):
        print("Valor incorreto")

gorjeta = -1
while gorjeta < 0 or gorjeta > 100:
    gorjeta = int(input("Informe o percentual do serviço, entre 0 e 100: "))
    if not (0 <= gorjeta <= 100):
        print("Valor incorreto")

mostraNaTela(calcularConta(valorConta, qtdPessoas, gorjeta))
