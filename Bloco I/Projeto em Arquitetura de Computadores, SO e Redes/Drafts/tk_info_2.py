import tkinter as tk
import tkinter.ttk as ttk
import psutil
import cpuinfo


def cpu_info():
    cores = psutil.cpu_count(logical=False)
    threads = int(psutil.cpu_count())
    cpu_name = cpuinfo.get_cpu_info()['brand_raw']
    return {'cores': cores, 'threads': threads, 'name_processor': cpu_name}


class PysysinfoguiApp:
    def __init__(self, master=None):
        # build ui
        self.notebook_pysysgameinfo = ttk.Notebook(master)
        self.cpu_detailed_info = ttk.Frame(self.notebook_pysysgameinfo)
        self.cpu_processor_info = ttk.Labelframe(self.cpu_detailed_info)
        self.processor_info_name = tk.Label(self.cpu_processor_info)
        self.processor_info_name.configure(justify='left', text='Name')
        self.processor_info_name.grid(sticky='e')
        self.processor_info_name.grid_propagate(0)
        self.processor_info_name_4 = tk.Label(self.cpu_processor_info)
        ProcessorName = tk.StringVar('')
        ProcessorName.set(cpu_info()['name_processor'])
        self.processor_info_name_4.configure(foreground='#000080', relief='groove', text='ProcessorName', textvariable=ProcessorName)
        self.processor_info_name_4.grid(column='1', padx='20', row='0', sticky='e')
        self.cpu_processor_info.configure(height='200', text='Processador', width='399')
        self.cpu_processor_info.grid()
        self.cpu_processor_info.grid_propagate(0)
        self.cpu_processor_info.columnconfigure('0', minsize='0', pad='0')
        self.cpu_clocks = ttk.Labelframe(self.cpu_detailed_info)
        self.cpu_clocks.configure(height='150', text='Clocks (Core 0)', width='197')
        self.cpu_clocks.grid(padx='2', row='1', sticky='w')
        self.cpu_clocks.columnconfigure('0', minsize='0', pad='0')
        self.cpu_cache = ttk.Labelframe(self.cpu_detailed_info)
        self.cpu_cache.configure(height='150', text='Cache', width='197')
        self.cpu_cache.grid(column='0', row='1', sticky='e')
        self.cpu_cache.columnconfigure('0', minsize='0', pad='0')
        self.cpu_count = ttk.Frame(self.cpu_detailed_info)
        self.cpu_count_coreText = ttk.Label(self.cpu_count)
        self.cpu_count_coreText.configure(anchor='center', justify='center', text='Cores')
        self.cpu_count_coreText.grid(column='0', padx='5', sticky='w')
        self.cpu_count_coreText.grid_propagate(0)
        self.cpu_count_coreText.rowconfigure('0', pad='0', weight='0')
        self.separator_core_thread = ttk.Separator(self.cpu_count)
        self.separator_core_thread.configure(orient='vertical')
        self.separator_core_thread.grid(column='2', row='0')
        self.separator_core_thread.grid_propagate(0)
        self.separator_core_thread.rowconfigure('0', pad='0', weight='0')
        self.cpu_count_thread = ttk.Label(self.cpu_count)
        self.cpu_count_thread.configure(anchor='center', justify='center', text='Threads')
        self.cpu_count_thread.grid(column='3', padx='5', row='0', sticky='e')
        self.cpu_count_thread.grid_propagate(0)
        self.cpu_count_thread.rowconfigure('0', pad='0', weight='0')
        self.cpu_count_cores = tk.Label(self.cpu_count)
        qtdRealCores = tk.IntVar()
        qtdRealCores.set(cpu_info()['cores'])
        self.cpu_count_cores.configure(foreground='#000080', relief='groove', textvariable=qtdRealCores, width='3')
        self.cpu_count_cores.grid(column='1', row='0')
        self.cpu_count_threads = tk.Label(self.cpu_count)
        qtdThreadCores = tk.IntVar()
        qtdThreadCores.set(cpu_info()['threads'])
        self.cpu_count_threads.configure(font='TkDefaultFont', foreground='#000080', relief='groove',
                                         textvariable=qtdThreadCores)
        self.cpu_count_threads.configure(width='3')
        self.cpu_count_threads.grid(column='4', row='0')
        self.cpu_count.configure(height='35', relief='flat', width='190')
        self.cpu_count.grid(column='0', pady='5', row='2')
        self.cpu_count.grid_propagate(0)
        self.cpu_count.columnconfigure('0', minsize='0', pad='0')
        self.menu_bottom = ttk.Frame(self.cpu_detailed_info)
        self.logo_img = ttk.Label(self.menu_bottom)
        self.logo_img.configure(anchor='center', font='{Arial} 14 {bold}', foreground='#808080', text='PySysInfo')
        self.logo_img.grid()
        self.app_version = ttk.Label(self.menu_bottom)
        self.app_version.configure(text='v. 0.1 Beta')
        self.app_version.grid(column='1', padx='50', row='0', sticky='w')
        self.menubutton_Tools = ttk.Menubutton(self.menu_bottom)
        self.menubutton_Tools.configure(direction='above', state='normal', text='Tools')
        self.menubutton_Tools.grid(column='2', row='0', sticky='w')
        self.button_1 = ttk.Button(self.menu_bottom)
        self.button_1.configure(text='Exit')
        self.button_1.grid(column='3', row='0', sticky='e')
        self.button_1.grid_propagate(0)
        self.menu_bottom.configure(height='40', padding='2', relief='groove', width='400')
        self.menu_bottom.grid(column='0', row='3', sticky='s')
        self.menu_bottom.rowconfigure('3', minsize='0')
        self.menu_bottom.columnconfigure('0', minsize='0', pad='0')
        self.cpu_detailed_info.configure(height='200', relief='groove', width='100')
        self.cpu_detailed_info.grid()
        self.notebook_pysysgameinfo.add(self.cpu_detailed_info, text='CPU')
        self.notebook_pysysgameinfo.configure(height='422', width='400')
        self.notebook_pysysgameinfo.grid()

        # Main widget
        self.mainwindow = self.notebook_pysysgameinfo

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = PysysinfoguiApp(root)
    app.run()

