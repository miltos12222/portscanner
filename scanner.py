import socket

def scan_port(host, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
        print(f"[OPEN] Port {port}")
    except:
        pass
    finally:
        s.close()

def main():
    target = input("Target IP or domain: ")
    print(f"Scanning {target}...\n")

    for port in range(20, 1025):
        scan_port(target, port)

if __name__ == "__main__":
    main()
