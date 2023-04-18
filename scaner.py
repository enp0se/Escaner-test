"""Esta libreria nos permite trabajar con puertos"""
import socket
""" Introducimos ip y puertos"""
host =input("Introduce la ip: ")
ports= input("Introduce el puerto (separdos con coma): ")

ports = ports.split(",")
""" Nos dice la cantidad de puertos introducidos"""
print(f"se escanearn los {len(ports)}puertos para la ip: {host}")

for port in ports:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host,int(port)))