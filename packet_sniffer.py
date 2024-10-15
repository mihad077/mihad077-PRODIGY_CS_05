from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP


# Callback function to process captured packets
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src  # Source IP
        ip_dst = packet[IP].dst  # Destination IP
        proto = packet[IP].proto  # Protocol number

        # If the packet is TCP
        if TCP in packet:
            sport = packet[TCP].sport  # Source port
            dport = packet[TCP].dport  # Destination port
            print(f"TCP Packet: Source IP {ip_src}:{sport}, Destination IP {ip_dst}:{dport}")

        # If the packet is UDP
        elif UDP in packet:
            sport = packet[UDP].sport  # Source port
            dport = packet[UDP].dport  # Destination port
            print(f"UDP Packet: Source IP {ip_src}:{sport}, Destination IP {ip_dst}:{dport}")

        # If it's another type of packet
        else:
            print(f"Other Packet: Source IP {ip_src}, Destination IP {ip_dst}, Protocol: {proto}")


# Capture and process 10 packets
print("Starting packet capture...")
sniff(prn=packet_callback, count=10)
