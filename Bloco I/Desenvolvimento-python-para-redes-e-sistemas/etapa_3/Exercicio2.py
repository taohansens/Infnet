import psutil
from psutil._common import bytes2human;


def lista_e_media():
    processos_psutil = psutil.process_iter()
    lista_de_processos = []
    soma = 0
    contador = 0
    for process in processos_psutil:
        try:
            info_process = process.as_dict(attrs=['pid', 'name', 'memory_info'])
            dict_process = {'pid': info_process['pid'], 'name': info_process['name'],
                            'memory': info_process['memory_info'].rss}
            soma += info_process['memory_info'].rss
            contador += 1
            lista_de_processos.append(dict_process)
        except psutil.NoSuchProcess:
            pass
    media = soma / contador
    return lista_de_processos, media


def acima_media(lista, media, percent):
    lista_resposta = []
    for process in lista:
        if process['memory'] > (media + media * percent / 100):
            lista_resposta.append(process)
    return lista_resposta


processos, media = lista_e_media()
print(f"A média de consumo é de {bytes2human(media)}.\n")

try:
    print("Digite a % de memória acima da média: ")
    porcentagem = int(input("Digite: "))
except ValueError:
    porcentagem = 10
    print(ValueError, "Exindo os processos com consumo acima de 10% da média.")

valor = media + media * porcentagem / 100
print(f"Exibindo os processos que consomem mais que {bytes2human(valor)}")

lista_resposta = acima_media(lista_e_media()[0], lista_e_media()[1], porcentagem)
templ = "%-6s %15s %15s | %5s"

print(templ % ("PID", "NOME", "MEMORY", "> ACIMA_MEDIA"))
# Ordenando lista por tamanho
ordenada = sorted(lista_resposta, key=lambda row: row['memory'], reverse=1)
for item in ordenada:
    print(templ % (item['pid'], item['name'], bytes2human(item['memory']), bytes2human(item['memory'] - valor)))
