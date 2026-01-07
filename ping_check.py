import os

def ping(ip):
    command = "ping -n 1" if os.name == "nt" else "ping -c 1"
    return os.system(f"{command} {ip}") == 0

ip = input("Введите IP-адрес: ")

if ping(ip):
    print(f"{ip} доступен")
else:
    print(f"{ip} недоступен")
