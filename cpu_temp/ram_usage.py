def get_memory_usage():
    with open("/proc/meminfo", "r") as file:
        lines = file.readlines()
    
    mem_total = int(lines[0].split()[1])
    mem_free = int(lines[1].split()[1])
    mem_available = int(lines[2].split()[1])
    mem_used = mem_total - mem_available
    
    return int(mem_used / 1024.0), int(mem_total / 1024.0)

