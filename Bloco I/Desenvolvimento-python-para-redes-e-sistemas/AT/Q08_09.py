import pprint
import threading
import time
from random import randint
from multiprocessing import Pool
import matplotlib.pyplot as plt

TEMPOS = {"SEQUENCIAL": {},
          "THREADING": {},
          "MULTI": {}}


def factorial(n):
    factorial = n
    for i in range(n - 1, 1, -1):
        factorial = factorial * i
    return (factorial)


def calc_fact(lis_en, start_t, end_t, lis_s):
    for i in range(start_t, end_t):
        lis_s.append(factorial(lis_en[i]))


def print_format(tipo, num, exec, time):
    if exec == 0:
        print(f"=== EXECUÇÃO {tipo}: {num} ===")
    print(f"EXEC {exec+1}: {time} segundos.")


def sequencial():
    for qtd_numero in [200000, 500000, 1000000]:
        execucao = 0
        TEMPOS["SEQUENCIAL"][qtd_numero] = []
        while execucao < 5:
            inicio = float(time.time())
            A = []
            B = []
            for i in range(qtd_numero):
                A.append(randint(1, 10))
            for item in A:
                B.append(factorial(item))
            fim = float(time.time())
            tempo = round(fim - inicio,5)
            # print_format("SEQUENCIAL", qtd_numero, execucao, tempo)
            TEMPOS["SEQUENCIAL"][qtd_numero].append(tempo)
            execucao += 1


def threadg():
    for qtd_numero in [200000, 500000, 1000000]:
        TEMPOS["THREADING"][qtd_numero] = []
        execucao = 0
        while execucao < 5:

            A = []
            B = []
            T = []
            threads = 4
            inicio = float(time.time())
            for i in range(qtd_numero):
                A.append(randint(1, 10))

            for i in range(threads):
                start_t = i * int(qtd_numero / threads)
                end_t = (i + 1) * int(qtd_numero / threads)
                th = threading.Thread(target=calc_fact, args=(A, start_t, end_t, B))
                th.start()
                T.append(th)

            for th in T:
                th.join()
            fim = float(time.time())
            tempo = round(fim - inicio, 5)
            TEMPOS["THREADING"][qtd_numero].append(tempo)
            # print_format("THREADING", qtd_numero, execucao, tempo)
            execucao += 1


def main():
    for qtd_numero in [200000, 500000, 1000000]:
        TEMPOS["MULTI"][qtd_numero] = []
        execucao = 0
        while execucao < 5:
            inicio = float(time.time())
            with Pool(processes=4) as pool:
                A = []
                for i in range(qtd_numero):
                    A.append(randint(1, 10))

                B = []
                for i in A:
                    B.append(factorial(i))
            fim = float(time.time())
            tempo = round(fim - inicio, 5)
            TEMPOS["MULTI"][qtd_numero].append(tempo)
            # print_format("MULTI", qtd_numero, execucao, tempo)
            execucao += 1


if __name__ == "__main__":
    main()

sequencial()
threadg()
pprint.pprint(TEMPOS)