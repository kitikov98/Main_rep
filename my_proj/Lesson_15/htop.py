import psutil


print(f"{'Load CPU':<13}|{psutil.cpu_percent(interval=1)}%")
load_proc = psutil.getloadavg()
print(f"{'Load average':<13}|{load_proc[0]:^6}{load_proc[1]:^6}{load_proc[2]:^6}")


virt_memt = psutil.virtual_memory()
virt_memt = virt_memt.total/(1024**2)
virt_memu = psutil.virtual_memory()
virt_memu = virt_memu.used/(1024**2)
print(f"{'Memory':<13}|{virt_memu:>.2f} / {virt_memt:.2f} MB")

sw_memt = psutil.swap_memory( )
sw_memt = sw_memt.total/(1024**2)
sw_memu = psutil.swap_memory( )
sw_memu = sw_memu.used/(1024**2)
print(f"{'SWP Memory':<13}|{sw_memu:>7.2f} / {sw_memt:.2f} MB")

print(f"{'running PID':<13}|{len(psutil.pids())}")


print("_"*100)
print(f"{'pid':_^10}{'username':^20}{'memory_percent':^16}{'cpu_percent':^16}{'cmdline'}")

for proc in psutil.process_iter(['pid','cmdline','username','memory_percent','cpu_percent']):
    if proc.info['cmdline'] == []:
        continue
    else:
        print(f"{proc.info['pid']:_^10}{proc.info['username']:^20}{proc.info['memory_percent']:^16.2f}{proc.info['cpu_percent']:^16.2f}{proc.info['cmdline']}")
