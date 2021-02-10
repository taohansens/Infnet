import subprocess
# https://docs.python.org/3/library/subprocess.html

# run Calc
print(subprocess.run("calc"))

# run notepad with args
print(subprocess.run(["notepad", "nome_do_arquivo.txt"]))


# retorna objeto com atr e func, ex: PID.
p = subprocess.Popen("notepad")
print(f"PID do projeto: {p.pid}")
