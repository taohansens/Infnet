import time

import psutil
from psutil._common import bytes2human

total_antes = psutil.net_io_counters()
total_adapter_antes = psutil.net_io_counters(pernic=True)
time.sleep(1)
total_depois = psutil.net_io_counters()
total_adapter_depois = psutil.net_io_counters(pernic=True)


adapters = list(total_adapter_depois.keys())
for adapter in adapters:
    status_antes = total_adapter_antes[adapter]
    status_depois = total_adapter_depois[adapter]
    templ = "%-15s %15s %15s"
    print(templ % (adapter, "TOTAL", "POR-SEG"))
    print(templ % (
        "Enviados (KB)",
        round(status_depois.bytes_sent/1024, 2),
        round((status_depois.bytes_sent - status_antes.bytes_sent)/1024, 2),
    ))
    print(templ % (
        "Recebidos (KB)",
        round(status_depois.bytes_recv/1024, 2),
        round((status_depois.bytes_recv - status_antes.bytes_recv)/1024, 2),
    ))
    print(templ % (
        "Pacotes Env.",
        status_depois.packets_sent,
        status_depois.packets_sent - status_antes.packets_sent,
    ))
    print(templ % (
        "Pacotes Rec.",
        status_depois.packets_recv,
        status_depois.packets_recv - status_antes.packets_recv,
    ))
    print("\n")