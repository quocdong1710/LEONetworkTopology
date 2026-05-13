FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    mininet \
    openvswitch-switch \
    openvswitch-common \
    hping3 \
    iperf3 \
    tcpdump \
    iputils-ping \
    net-tools \
    curl \
    wget \
    nano \
    vim \
    sudo \
    dos2unix \
    && apt-get clean

WORKDIR /app

COPY . /app

# Fix shell script permissions
RUN chmod +x /app/LEO/attack.sh || true

# Fix Windows CRLF
RUN dos2unix /app/LEO/attack.sh || true

CMD ["/bin/bash"]