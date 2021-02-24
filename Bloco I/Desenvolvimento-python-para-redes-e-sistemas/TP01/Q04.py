# Q04 Que função do módulo ‘os’ de Python é usada para obter o caminho absoluto de um diretório
# com caminho relativo? Dê um exemplo.

# Importando módulo os.
import os
from os.path import join, normpath

path = '../TP01'

# https://docs.python.org/3.6/library/os.path.html#os.path.abspath
print("os.path.abspath(path) :\n " + os.path.abspath(path))

# é equivalente à linha abaixo:
print("\nnormpath(join(os.getcwd(), path)) :\n" + normpath(join(os.getcwd(), path)))
