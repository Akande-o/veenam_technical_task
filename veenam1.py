import psutil
import time
import os

details_dict = {"CPU":[], "memory": [], "file_handles": []}
def processcheck(seekitem):
    return seekitem in (p.name().lower() for p in psutil.process_iter())

#print(processcheck("System"))
#print(psutil.cpu_percent(interval = 1.0, percpu = True))
#print(psutil.virtual_memory())
def process(filepath, interval):
    os.system(filepath)
    exec_file = os.path.basename(filepath)
    while processcheck(exec_file):
        processoutput(filepath, interval)
    return details_dict

def processoutput(filepath, interval):
    cpu_percent = psutil.cpu_percent(interval = 1.0, percpu = True)
    mem = psutil.virtual_memory()
    for p in psutil.process_iter():
        if os.path.basename(filepath) == p.name().lower():
            num = len(p.open_files())
            break
        else:
            continue
    print(cpu_percent, mem, num)
    details_dict["CPU"].append(cpu_percent)
    details_dict["memory"].append(mem[3:])
    details_dict["file_handles"].append(num)
    time.sleep(interval)

print(process("C:/Users/Akande/Downloads/chrome.exe", 0.5))



