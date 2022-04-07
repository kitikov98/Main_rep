import psutil


def load_cpu():
    return ('Load CPU (%)', psutil.cpu_percent(interval=1))
    # print(f"{'Load CPU':<21}|{psutil.cpu_percent(interval=1):^6}%")

def load_proc():
    load_proc = psutil.getloadavg()
    return ('Load average', load_proc[0], load_proc[1],load_proc[2])
    # print(f"{'Load average':<21}|{load_proc[0]:^6}{load_proc[1]:^6}{load_proc[2]:^6}")

def virt_mem():
    virt_memt = psutil.virtual_memory()
    virt_memt = round(virt_memt.total/(1024**2),2)
    virt_memu = psutil.virtual_memory()
    virt_memu = round(virt_memu.used/(1024**2),2)
    return ('Memory (MB)', virt_memu, virt_memt)
    # print(f"{'Memory':<21}|{virt_memu:^9.2f}/{virt_memt:^9.2f} MB")

def swp_mem():
    sw_memt = psutil.swap_memory( )
    sw_memt = round(sw_memt.total/(1024**2),2)
    sw_memu = psutil.swap_memory( )
    sw_memu = round(sw_memu.used/(1024**2),2)
    return ('SWP Memory (MB)', sw_memu, sw_memt)
    # print(f"{'SWP Memory':<21}|{sw_memu:^6.2f} / {sw_memt:.2f} MB")

def run_pid():
    return ('running PID', len(psutil.pids()))
    # print(f"{'running PID':<21}|{len(psutil.pids()):^6}")

def htop_proc():
    # print("_"*100)
    # print(f"{'pid':_^16}{'username':^16}{'memory_percent':^16}{'cpu_percent':^16}{'cmdline'}")

    for proc in psutil.process_iter(['pid','cmdline','username','memory_percent','cpu_percent']):
        if proc.info['cmdline'] == []:
            continue
        else:
            print(f"{proc.info['pid']:<16}{proc.info['username']:^16}{proc.info['memory_percent']:^16.2f}{proc.info['cpu_percent']:^16.2f}{proc.info['cmdline']}")

def netmb_inf():
    bytes_s = psutil.net_io_counters( )
    bytes_s = bytes_s.bytes_sent/(1024**2)
    bytes_r = psutil.net_io_counters( )
    bytes_r = bytes_r.bytes_recv/(1024**2)
    # print(f"{'MB sent/rec':<21}|{bytes_s:^6.2f}/{bytes_r:.2f} MB")
    return ('MB sent/rec (MB)', bytes_s, bytes_r)

def netpack_inf():
    pack_s = psutil.net_io_counters( )
    pack_s = pack_s.packets_sent
    pack_r = psutil.net_io_counters( )
    pack_r = pack_r.packets_recv
    # print(f"{'Packets sent/rec':<21}|{pack_s:^6}/{pack_r}")
    return ('Packets sent/rec', pack_s, pack_r)

def disk_inf():
    disk_u = psutil.disk_usage('/')
    disk_u = round(disk_u.used/(1024**2),2)
    disk_t = psutil.disk_usage('/')
    disk_t = round(disk_t.total/(1024**2),2)
    disk_f = psutil.disk_usage('/')
    disk_f = round(disk_f.free / (1024 ** 2),2)
    # print(f"{'Disk total/used/free':<21}|{disk_t:^10.2f}/{disk_u:^10.2f}/{disk_f:^8.2f} MB")
    return ('Disk total/used/free (MB)',disk_t,disk_u,disk_f)

def full_info():
    title_s={disk_inf()[0]:disk_inf()[1:],
              netpack_inf()[0]:netpack_inf()[1:],
              run_pid()[0]:run_pid()[1:],
              swp_mem()[0]:swp_mem()[1:],
              virt_mem()[0]: virt_mem()[1:],
              load_proc()[0]: load_proc()[1:],
              load_cpu()[0]: load_cpu()[1:],
             }
    return title_s
    # print(title_s)

def info_viev():
    htop_proc()
    info = full_info()
    for k in info.keys():
        i = info.get(k)
        print(f'{k:<30}|', end='')
        for j in i:
            print(f'{j:^10}|', end='')
        print()



info_viev()
