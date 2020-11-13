def diagnostico(renda, valor_gasto, recomendado, tipo):
    valormargem = renda * (recomendado / 100)
    if valor_gasto < valormargem:
        print("Seus gastos totais com {} comprometem {:.1f}% de sua renda total. "
              "O máximo recomendado é de {}%. Seus gastos estão dentro da margem recomendada.".format(tipo, (valor_gasto/renda*100),
                                                                                                      recomendado))
    else:
        print("Seus gastos totais com {} comprometem {:.1f}% de sua renda total. "
              "O máximo recomendado é de {}%. Portanto, idealmente, o máximo de sua renda "
              "comprometida com moradia deveria ser de R$ {:.2f}.".format(tipo, (valor_gasto/renda*100), recomendado, renda * (recomendado/100)))


# Valores máximos recomendados em (%)
recom_moradia = 30
recom_educa = 20
recom_trans = 15

renda_mensal = float(input("Renda mensal total: R$"))
gastos_moradia = float(input("Gastos totais com moradia: R$"))
gastos_educacao = float(input("Gastos totais com educação: R$"))
gastos_transporte = float(input("Gastos totais com transporte: R$"))

diagnostico(renda_mensal, gastos_moradia, recom_moradia, "moradia")
diagnostico(renda_mensal, gastos_educacao, recom_educa, "educação")
diagnostico(renda_mensal, gastos_transporte, recom_trans, "transporte")
