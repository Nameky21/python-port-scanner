import socket

def scan_port(target, port, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((target, port)) == 0


def scan_ports(target, ports, timeout=1):
    open_ports = []
    for port in ports:
        if scan_port(target, port, timeout):
            open_ports.append(port)
    return open_ports
