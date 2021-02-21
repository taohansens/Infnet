import tkinter as tk
import tkinter.ttk as ttk
import psutil


def cpu_info():
    cores = psutil.cpu_count(logical=False)
    threads = int(psutil.cpu_count())
    return {'cores': cores, 'threads': threads}


class PySysInfo:

    def __init__(self, master=None):
        # build ui
        self.notebook_4 = ttk.Notebook(master)
        self.CPU_Frame = ttk.Frame(self.notebook_4)
        self.cpu_processor = ttk.Labelframe(self.CPU_Frame)
        self.cpu_processor.configure(height='200', padding='0', relief='groove', text='Processador')
        self.cpu_processor.configure(width='395')
        self.cpu_processor.grid(padx='2')
        self.cpu_clocks = ttk.Labelframe(self.CPU_Frame)
        self.cpu_clocks.configure(height='150', padding='0', relief='groove', text='Clocks (Core #0)')
        self.cpu_clocks.configure(width='180')
        self.cpu_clocks.grid(padx='2', sticky='w')
        self.cpu_clocks_17 = ttk.Labelframe(self.CPU_Frame)
        self.cpu_clocks_17.configure(height='150', padding='10', relief='groove', text='Clocks (Core #0)')
        self.cpu_clocks_17.configure(width='210')
        self.cpu_clocks_17.grid(column='0', padx='2', row='1', sticky='e')
        self.cpu_clocks_20 = ttk.Labelframe(self.CPU_Frame)
        self.cpu_cores = ttk.Label(self.cpu_clocks_20)
        self.cpu_cores.configure(text='Cores')
        self.cpu_cores.grid(column='0', padx='15', row='0')
        self.cpu_cores_qtd = tk.Label(self.cpu_clocks_20)
        qtdRealCores = tk.IntVar()
        qtdRealCores.set(cpu_info()['cores'])
        self.cpu_cores_qtd.configure(foreground='#000080', highlightbackground='#000080', highlightcolor='#000080', justify='center')
        self.cpu_cores_qtd.configure(padx='5', relief='groove', state='normal', textvariable=qtdRealCores)
        self.cpu_cores_qtd.grid(column='1', row='0')
        self.cpu_threads = ttk.Label(self.cpu_clocks_20)
        self.cpu_threads.configure(text='Threads')
        self.cpu_threads.grid(column='2', padx='15', row='0')
        self.cpu_threads_qtd = tk.Label(self.cpu_clocks_20)
        qtdRealThreads = tk.IntVar()
        qtdRealThreads.set(cpu_info()['threads'])
        self.cpu_threads_qtd.configure(foreground='#000080', highlightbackground='#000080', highlightcolor='#000080', justify='right')
        self.cpu_threads_qtd.configure(padx='5', relief='groove', state='normal', textvariable=qtdRealThreads)
        self.cpu_threads_qtd.grid(column='3', padx='5', row='0')
        self.cpu_clocks_20.configure(height='40', padding='0', relief='groove', width='395')
        self.cpu_clocks_20.grid(padx='2', row='2')
        self.cpu_clocks_20.rowconfigure('2', minsize='0')
        self.CPU_Frame.configure(height='200', width='200')
        self.CPU_Frame.grid(row='0')
        self.CPU_Frame.grid_propagate(0)
        self.notebook_4.add(self.CPU_Frame, compound='top', text='CPU')
        self.notebook_4.configure(height='400', width='400')
        self.notebook_4.grid()

        # Main widget
        self.mainwindow = self.notebook_4


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = PySysInfo(root)
    app.run()

