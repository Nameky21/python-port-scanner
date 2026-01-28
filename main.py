import argparse
from scanner.port_scanner import scan_port
from scanner.utils import threaded_scan
from scanner.ttl_fingerprint import get_ttl, guess_os

def parse_ports(port_range):
    if "-" in port_range:
        start, end = map(int, port_range.split("-"))
        return range(start, end + 1)
    return [int(port_range)]

def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner with TTL OS Fingerprinting")
    parser.add_argument("--target", required=True, help="Target IP or hostname")
    parser.add_argument("--ports", default="1-1024", help="Port or range (e.g. 80 or 1-1024)")
    parser.add_argument("--os-detect", action="store_true", help="Enable OS fingerprinting")

    args = parser.parse_args()
    ports = parse_ports(args.ports)

    print(f"[+] Scanning {args.target}...")

    open_ports = threaded_scan(scan_port, args.target, ports)
    print(f"[+] Open ports: {open_ports if open_ports else 'None'}")

    if args.os_detect:
        ttl = get_ttl(args.target)
        os_guess = guess_os(ttl)
        print(f"[+] Observed TTL: {ttl}")
        print(f"[+] OS Guess: {os_guess}")

if __name__ == "__main__":
    main()
