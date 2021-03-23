import psutil
from psutil._common import bytes2human


def processos():
    processos_psutil = psutil.process_iter()
    lista_de_processos = []
    for process in processos_psutil:
        try:
            info_process = process.as_dict(attrs=['pid', 'name', 'memory_info', 'cpu_percent'])
            dict_process = {'pid': info_process['pid'],
                            'name': info_process['name'],
                            'memory': info_process['memory_info'],
                            'cpu': info_process['cpu_percent']}
            lista_de_processos.append(dict_process)
        except psutil.NoSuchProcess:
            pass
    return lista_de_processos


FORMAT = "%-25s %5s %8s %6s"
TOP = "%-25s %5s %8s %2s" % ("NOME", "PID", "MEMÓRIA", "USO CPU")


def main():
    while True:
        lista_de_processos = processos()
        print(TOP)
        for p in lista_de_processos:
            print(FORMAT % (p['name'][:25], p['pid'], bytes2human(p['memory'].rss), str(p['cpu'])+'%'))


if __name__ == "__main__":
    main()
