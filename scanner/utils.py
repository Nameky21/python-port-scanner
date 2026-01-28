from concurrent.futures import ThreadPoolExecutor, as_completed

def threaded_scan(scan_func, target, ports, workers=100):
    results = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(scan_func, target, port): port
            for port in ports
        }

        for future in as_completed(futures):
            port = futures[future]
            if future.result():
                results.append(port)

    return sorted(results)
