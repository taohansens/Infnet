# Create 10 exceptions.
# https://docs.python.org/3/library/exceptions.html

# Division by Zero
def um():
    try:
        a = 100 / 0
    except ZeroDivisionError as e:
        print(e)


# NameError
def dois():
    try:
        return x
    except NameError as e:
        print(type(e), e)


# IndexError
def tres():
    try:
        len = [1]
        return len[1]
    except IndexError as e:
        print(type(e), e)


# KeyError
def quatro():
    try:
        dicionario = {'arvore': 1}
        return dicionario['planta']
    except KeyError as e:
        print(type(e), e)


# ModuleNotFoundError
def cinco():
    try:
        import py_game
    except ModuleNotFoundError as e:
        print(type(e), e)


# AttributeError
def seis():
    try:
        x = 'xd'.lenfg()
    except AttributeError as e:
        print(type(e), e)


# Import Error
def sete():
    try:
        from psutil import common
    except ImportError as e:
        print(type(e), e)


# FileNotFoundError
def oito():
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as e:
        print(type(e), e)


# PermissionError
def nove():
    try:
        with open('../etapa_3') as file:
            read_data = file.read()
    except PermissionError as e:
        print(type(e), e)


# RecursionError
def dez():
    try:
        def a():
            return a()

        a()
    except RecursionError as e:
        print(type(e), e)

