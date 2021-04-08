# #
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import seaborn as sns

# sns.set_theme(style="whitegrid")
#
# rs = np.random.RandomState(365)
# values = rs.randn(365, 4).cumsum(axis=0)
# dates = pd.date_range("1 1 2016", periods=365, freq="D")
# data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
# data = data.rolling(7).mean()
#
# sns.lineplot(data=data, palette="tab10", linewidth=2.5)
#
qtd = [n for n in range(1, 6)]
print(qtd)
# {'MULTI': {200000: [0.25106, 0.26606, 0.25206, 0.26706, 0.26206],
#            500000: [0.63051, 0.64595, 0.63214, 0.65315, 0.62914],
#            1000000: [1.26879, 1.22428, 1.34156, 1.3133, 1.28729]},
#  'SEQUENCIAL': {200000: [0.22006, 0.21305, 0.21005, 0.21205, 0.21105],
#                 500000: [0.53012, 0.53612, 0.53212, 0.53212, 0.54712],
#                 1000000: [1.08624, 1.08304, 1.08718, 1.08875, 1.07713]},
#  'THREADING': {200000: [0.23383, 0.23911, 0.23206, 0.23906, 0.23607],
#                500000: [0.57883, 0.57713, 0.62614, 0.57713, 0.57013],
#                1000000: [1.16526, 1.17017, 1.17526, 1.25728, 1.20727]}}
#





# KEYS = [n for n in mydict.keys()]
# for chave in KEYS:
#     df = pd.DataFrame(list(mydict[chave].items()), columns=['TIPO', 'N'])
# sns.lineplot(data=df, x=)


import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
  # white noise 2

# Two signals with a coherent part at 10Hz and a random part
mult = [1.26879, 1.22428, 1.34156, 1.3133, 1.28729]
seq = [1.08624, 1.08304, 1.08718, 1.08875, 1.07713]
thr = [1.16526, 1.17017, 1.17526, 1.25728, 1.20727]

# plt.plot(qtd, mult, 'r--', qtd, seq, qtd, thr, linewidth=3.0)
plt.title("N = 1.000.000 Factorials")
plt.plot(qtd, mult, 'b', label='Multiprocessing', linewidth=3.0)
plt.plot(qtd, thr, 'g', label='Threading', linewidth=3.0)
plt.plot(qtd, seq, 'r', label='Sequencial', linewidth=3.0)
plt.legend()
plt.xlim(1, 5)
plt.xlabel('Execução')
plt.ylabel('Tempo (s)')
plt.grid(True)
#
# cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
# axs[1].set_ylabel('coherence')

plt.tight_layout()
plt.xticks(qtd)
plt.show()


TEMPO = {'MULTI': {1000000: [1.40986, 1.3393, 1.3453, 1.30683, 1.34232],
           5000000: [6.7098, 6.51747, 6.36446, 6.6695, 6.64049],
           10000000: [14.42132, 14.12794, 13.91099, 13.36701, 13.83688]},
 'SEQUENCIAL': {1000000: [1.15126, 1.12025, 1.13025, 1.14926, 1.10225],
                5000000: [5.58483, 5.58535, 5.60249, 5.63827, 5.60526],
                10000000: [11.18835, 11.28496, 11.39008, 11.22016, 11.37318]},
 'THREADING': {1000000: [1.17877, 1.26728, 1.20827, 1.21227, 1.19827],
               5000000: [5.94134, 5.99204, 6.15085, 6.07937, 5.93171],
               10000000: [12.17264, 11.84312, 11.90104, 12.10143, 11.81854]}}


def cria_grafico(tempos):




cria_grafico(TEMPO)