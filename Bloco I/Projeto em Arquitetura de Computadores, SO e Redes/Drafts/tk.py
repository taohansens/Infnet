# Importar modulo Tkinter
import tkinter as tk
from tkinter import ttk

# Tamanho da tela
HEIGHT = 400
WIDTH = 400

window = tk.Tk()
window.geometry(f'{HEIGHT}x{WIDTH}')
window.title("PySysInfo")

# Abas
tab_control = ttk.Notebook(window)

'''
Info Procesador
'''
tab_cpu = ttk.Frame(tab_control)
tab_control.add(tab_cpu, text='CPU')
lbl1 = tk.Label(tab_cpu, text='CPU')


'''
Info Memória
'''
tab_memory = ttk.Frame(tab_control)
tab_control.add(tab_memory, text='Memória')
lbl2 = tk.Label(tab_memory, text='Memória')

'''
Info Discos
'''
tab_disks = ttk.Frame(tab_control)
tab_control.add(tab_disks, text='Discos')
lbl3 = tk.Label(tab_disks, text='Discos')

'''
Info Rede
'''
tab_network = ttk.Frame(tab_control)
tab_control.add(tab_network, text='Rede')
lbl4 = tk.Label(tab_network, text='Rede')


lbl1.grid(column=0, row=0)
lbl2.grid(column=1, row=0)
lbl3.grid(column=2, row=0)
lbl4.grid(column=3, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()

