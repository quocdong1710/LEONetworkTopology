# DDoS Attack Simulation

This project supports multiple DDoS attack simulations against the Ground Station (`h_hcm`) in the LEO satellite network topology using `hping3`.

## Requirements

Install `hping3`:

```bash
sudo apt update
sudo apt install hping3 -y
```

Grant execute permission:

```bash
chmod +x attack.sh
```

---

# Run Attack Tool

Inside Mininet CLI:

```bash
attacker ./attack.sh
```

---

# Available Attack Modes

| Mode | Description |
|---|---|
| ICMP Flood | Flood ICMP packets to saturate uplink bandwidth |
| UDP Flood | Flood UDP packets to overload satellite traffic channel |
| TCP SYN Flood | Flood TCP SYN packets to exhaust connection resources |
| TCP FIN Flood | Flood FIN packets to disrupt TCP sessions |
| TCP RST Flood | Flood RST packets to terminate active connections |
| LAND Attack | Spoof target IP as source IP |
| Fragment Flood | Send fragmented packets to increase packet processing overhead |

---

# Example

```bash
mininet> attacker ./attack.sh
```

Select attack mode:

```text
1) ICMP Flood
2) UDP Flood
3) TCP SYN Flood
4) TCP FIN Flood
5) TCP RST Flood
6) LAND Attack
7) Fragment Flood
```

Example:

```text
Select attack mode: 2
```

This will start a UDP Flood attack against the Ground Station (`10.0.100.1`).

---

# Monitor Network Impact

Check latency and packet loss:

```bash
h_hcm ping 10.0.3.1
```

Check queue congestion and dropped packets:

```bash
h_hcm tc -s qdisc
```

Monitor encrypted traffic:

```bash
h_sing python3 receiver.py
```

During DDoS attacks, the receiver may experience:

- Increased latency
- Packet loss
- AES-GCM decrypt failures
- Queue congestion
- Uplink saturation