FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    mininet \
    iproute2 \
    iputils-ping \
    net-tools \
    hping3 \
    tcpdump \
    openvswitch-switch \
    && apt-get clean

WORKDIR /app

COPY . /app

# Fix shell script permissions
RUN chmod +x /app/LEO/attack.sh || true

# Fix Windows CRLF
RUN dos2unix /app/LEO/attack.sh || true

CMD ["/bin/bash"]