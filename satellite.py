# satellite.py 
import socket
import sys

if len(sys.argv) < 4:
    print("Usage: python3 satellite.py <my_listen_ip> <forward_ip> <port>")
    sys.exit(1)

listen_ip = sys.argv[1]
forward_ip = sys.argv[2]
port = int(sys.argv[3])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((listen_ip, port))

print(f"[Satellite] Listening on {listen_ip}:{port} → Forward to {forward_ip}:{port}")

while True:
    data, addr = sock.recvfrom(4096)
    print(f"[Satellite] Forwarded {len(data)} bytes from {addr[0]}")
    sock.sendto(data, (forward_ip, port))