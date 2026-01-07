import os

ip = input("Введите IP-адрес: ")
response = os.system(f"ping -n 1 {ip}" if os.name == "nt" else f"ping -c 1 {ip}")

if response == 0:
    print(f"{ip} доступен")
else:
    print(f"{ip} недоступен")
