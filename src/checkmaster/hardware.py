import psutil


def get_cpus() -> int:
    return cpu_count()

def get_ram(unit="MB") -> int:
    res = psutil.virtual_memory().total  # total physical memory available in Bytes
    if unit.lower() == "gb":
        res = ((res / 1024) / 1024) / 1024
    elif unit.lower() == "mb":
        res =  (res / 1024) / 1024
    elif unit.lower() == "kb":
        res = res / 1024
    return int(res)