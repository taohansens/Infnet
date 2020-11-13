def verificaSituacaoEleitoral(idade):
    if idade < 16:
        print("Não tem direito a voto.")
    elif (16 <= idade < 18) or (idade >= 70):
        print("Não tem obrigação de votar.")
    elif 18 <= idade < 70:
        print("Tem obrigação de votar.")

idade = 0
while idade <= 0:
    idade = int(input("Informe a idade: "))
    if not (idade > 0):
        print(ValueError("Essa idade é inválida."))

verificaSituacaoEleitoral(idade)
