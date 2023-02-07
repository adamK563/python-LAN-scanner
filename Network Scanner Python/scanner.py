import socket
import sys

def get_host_name(ip):
    try:
        host_name = socket.gethostbyaddr(ip)[0]
        return host_name
    except:
        return "Unknown"

def scan_network(ip_range):
    for i in range(1, 256):
        ip = ip_range + str(i)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, 135))
        if result == 0:
            print(f"{ip} is active. Hostname: {get_host_name(ip)}")
        else:
            print(f"{ip} is inactive")
        sock.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        network_prefix = sys.argv[1]
        scan_network(network_prefix)
    else:
        print("Usage: python network_scanner.py <network_prefix>")
        print("Example: python network_scanner.py 192.168.1.")

# Common network prefixes used for local area networks (LANs):

# python scanner.py 10.0.0.
# python scanner.py 172.16.0.
# python scanner.py 192.168.0.
# python scanner.py 192.168.1. 
# python scanner.py 192.168.10.
# ...
# python scanner.py 192.168.100.
# python scanner.py 192.168.101.
# python scanner.py 192.168.102.
# python scanner.py 192.168.103.
# python scanner.py 192.168.104.
# ...
# python scanner.py 192.168.255.
