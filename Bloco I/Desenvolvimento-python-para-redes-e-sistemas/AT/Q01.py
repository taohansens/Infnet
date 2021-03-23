import psutil


def processos():
    processos_psutil = psutil.process_iter()
    lista_de_processos = []
    for process in processos_psutil:
        try:
            info_process = process.as_dict(attrs=['pid', 'name'])
            dict_process = {'pid': info_process['pid'],
                            'name': info_process['name']}
            lista_de_processos.append(dict_process)
        except psutil.NoSuchProcess:
            pass
    return lista_de_processos


FORMAT = "%-25s %5s"
TOP = "%-25s %5s" % ("NOME", "PID")


def main():
    lista_de_processos = processos()
    print(TOP)
    for p in lista_de_processos:
        print(FORMAT % (p['name'][:25], p['pid']))


if __name__ == "__main__":
    main()
