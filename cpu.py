import psutil

a = psutil.cpu_times()
print(a)

for x in range(3):
    a = psutil.cpu_percent(interval=1)
    print(a)

for x in range(3):
    a = psutil.cpu_percent(interval=1, percpu=True)
    print(a)

a = psutil.cpu_count()
print(a)

a = psutil.cpu_count(logical=False)
print(a)

a = psutil.cpu_freq()
print(a)

a = psutil.virtual_memory()
print(a)