# receiver.py - Ground Station Singapore
import socket

PORT = 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('10.0.3.1', PORT))

print("[Receiver Singapore] Listening on 10.0.3.1:9000")

while True:
    data, addr = sock.recvfrom(4096)
    try:
        payload = data[7:] if len(data) > 7 else data  # bỏ header đơn giản
        print(f"[RX] Received {len(data)} bytes from {addr[0]} | Payload: {payload.decode(errors='ignore')}")
    except:
        print(f"[RX] Received {len(data)} bytes from {addr[0]}")