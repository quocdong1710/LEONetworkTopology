# sender.py - Ground Station HCMC
import socket
import sys
import time
import struct
import os

SAT_HOST = "10.0.1.2"   # Sat1
SAT_PORT = 9000
KEY_HOST = "10.0.3.1"   # Singapore 
KEY_PORT = 9100

MESSAGES = [
    b"GS46-HCMC | COORD: 10.75N 106.67E | STATUS: OPERATIONAL",
    b"GS46-HCMC | UPLINK-TOKEN: X7F2-K9QM-3T1A | AUTH: VALID",
    b"GS46-HCMC | CMD: SAT-042 ADJUST ORBIT +0.5deg",
]

PACKET_COUNT = 10
INTERVAL_S = 0.5

def build_plain_packet(seq, payload):
    return struct.pack("!BIH", 0x01, seq, len(payload)) + payload

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "plain"
    print(f"Starting Sender (HCMC) in {mode.upper()} mode...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for seq in range(PACKET_COUNT):
        msg = MESSAGES[seq % len(MESSAGES)]
        pkt = build_plain_packet(seq, msg)
        sock.sendto(pkt, (SAT_HOST, SAT_PORT))
        print(f"[TX #{seq:02d}] Sent {len(pkt)} bytes to Sat1")
        time.sleep(INTERVAL_S)

    sock.close()
    print("Sender finished.")

if __name__ == "__main__":
    main()