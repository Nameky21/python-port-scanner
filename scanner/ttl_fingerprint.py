import subprocess
import platform
import re

def get_ttl(target):
    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", "1", target]
        ttl_pattern = r"TTL=(\d+)"
    else:
        cmd = ["ping", "-c", "1", target]
        ttl_pattern = r"ttl=(\d+)"

    try:
        output = subprocess.check_output(
            cmd,
            stderr=subprocess.DEVNULL,
            universal_newlines=True
        )
        match = re.search(ttl_pattern, output)
        if match:
            return int(match.group(1))
    except subprocess.CalledProcessError:
        pass

    return None


def guess_os(ttl):
    if ttl is None:
        return "Unknown"

    if ttl <= 64:
        return "Linux / macOS"
    elif ttl <= 128:
        return "Windows"
    else:
        return "Network Device / Router"
