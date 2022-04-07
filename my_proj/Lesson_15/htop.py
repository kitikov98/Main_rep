import psutil


def load_cpu():
    print(f"{'Load CPU':<21}|{psutil.cpu_percent(interval=1):^6}%")


def load_proc():
    load_proc = psutil.getloadavg()
    print(f"{'Load average':<21}|{load_proc[0]:^6}{load_proc[1]:^6}{load_proc[2]:^6}")

def virt_mem():
    virt_memt = psutil.virtual_memory()
    virt_memt = virt_memt.total/(1024**2)
    virt_memu = psutil.virtual_memory()
    virt_memu = virt_memu.used/(1024**2)
    print(f"{'Memory':<21}|{virt_memu:^9.2f}/{virt_memt:^9.2f} MB")


def swp_mem():
    sw_memt = psutil.swap_memory( )
    sw_memt = sw_memt.total/(1024**2)
    sw_memu = psutil.swap_memory( )
    sw_memu = sw_memu.used/(1024**2)
    print(f"{'SWP Memory':<21}|{sw_memu:^6.2f} / {sw_memt:.2f} MB")

def run_pid():
    print(f"{'running PID':<21}|{len(psutil.pids()):^6}")

def htop_proc():
    # print("_"*100)
    print(f"{'pid':_^10}{'username':^20}{'memory_percent':^16}{'cpu_percent':^16}{'cmdline'}")

    for proc in psutil.process_iter(['pid','cmdline','username','memory_percent','cpu_percent']):
        if proc.info['cmdline'] == []:
            continue
        else:
            print(f"{proc.info['pid']:_^10}{proc.info['username']:^20}{proc.info['memory_percent']:^16.2f}{proc.info['cpu_percent']:^16.2f}{proc.info['cmdline']}")


def netmb_inf():
    bytes_s = psutil.net_io_counters( )
    bytes_s = bytes_s.bytes_sent/(1024**2)
    bytes_r = psutil.net_io_counters( )
    bytes_r = bytes_r.bytes_recv/(1024**2)
    print(f"{'MB sent/rec':<21}|{bytes_s:^6.2f}/{bytes_r:.2f} MB")

def netpack_inf():
    pack_s = psutil.net_io_counters( )
    pack_s = pack_s.packets_sent
    pack_r = psutil.net_io_counters( )
    pack_r = pack_r.packets_recv
    print(f"{'Packets sent/rec':<21}|{pack_s:^6}/{pack_r}")



def disk_inf():
    disk_u = psutil.disk_usage('/')
    disk_u = disk_u.used/(1024**2)
    disk_t = psutil.disk_usage('/')
    disk_t = disk_t.total/(1024**2)
    disk_f = psutil.disk_usage('/')
    disk_f = disk_f.free / (1024 ** 2)
    print(f"{'Disk total/used/free':<21}|{disk_t:^10.2f}/{disk_u:^10.2f}/{disk_f:^8.2f} MB")



htop_proc()
run_pid()
load_proc()
load_cpu()
swp_mem()
virt_mem()
disk_inf()
netmb_inf()
netpack_inf()

