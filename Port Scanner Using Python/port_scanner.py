import socket
import threading
import argparse

# Lock for clean multithreaded output
print_lock = threading.Lock()

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # 1 second timeout
            result = s.connect_ex((host, port))
            if result == 0:
                with print_lock:
                    print(f"[+] Port {port} is OPEN")
    except Exception as e:
        with print_lock:
            print(f"[-] Error on port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("host", help="Target IP address or hostname")
    parser.add_argument("-p1", "--start-port", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-p2", "--end-port", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads (default: 100)")

    args = parser.parse_args()
    target_ip = socket.gethostbyname(args.host)
    print(f"[*] Scanning {args.host} ({target_ip}) from port {args.start_port} to {args.end_port}...\n")

    threads = []
    for port in range(args.start_port, args.end_port + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()
        if len(threads) >= args.threads:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    print("\n[✓] Scan complete.")

if __name__ == "__main__":
    main()
