import socket
from concurrent.futures import ThreadPoolExecutor

def port_scan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        if sock.connect_ex((ip, port)) == 0:
            print(f"TCP/{port} is open")
    except Exception as e:
        pass 
    finally:
        sock.close()

def main(speed, ip, a, z):
    if a >= z:
        print("Starting port must be less than ending port.")
        return

    ports = range(a, z)

    with ThreadPoolExecutor(int(speed)) as executor:
        for port in ports:
            executor.submit(port_scan, ip, port)

try:
    speed = int(input("Enter scan speed (1-100): "))
    a = int(input("Enter starting port: "))
    z = int(input("Enter ending port: "))
    ip = input("Enter IP address: ")
    main(speed, ip, a, z)
except ValueError:
    print("Invalid input! Ports and speed must be numbers.")
