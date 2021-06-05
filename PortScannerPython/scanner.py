from socket import *

main_ports = [21, 80, 8080, 3306, 5432, 4455]
open_ports = []

def connection(ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.2)
    code = s.connect_ex((ip, port))

    return code


def start(ip):
    for port in main_ports:
        code = connection(ip, port)

        if code == 0:
            open_ports.append(port)

    if len(open_ports) > 0:
        print("-----------------------------")
        print(f"IP: {ip}")

        for port in open_ports:
            print(f"PORT -> {port} OPEN")


for i in range(100, 111):
    ip = f'192.168.1.{i}'
    start(ip)

