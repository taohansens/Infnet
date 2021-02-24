# Q13 Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele.

# Importa o módulo subprocess
import subprocess

# Abre com o Popen, e retorna o PID
process = subprocess.Popen("calc").pid

print(f"PID: {process}")
