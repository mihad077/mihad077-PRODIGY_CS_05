PRODIGY_CS_05

Network Packet Analyzer

This project is a simple network packet sniffer written in Python. It captures network traffic and analyzes network packets, displaying relevant information such as:

Source IP Address

Destination IP Address

Protocol

Payload Data

Features
Captures live network packets

Displays detailed information for each packet, including source/destination IPs, protocols, and payloads

Supports multiple protocols (TCP, UDP, ICMP)

Flexible for further enhancement and testing

Installation
To install the required dependencies and run the project, follow these steps:

Clone the repository: git clone https://github.com/mihad077/mihad077-PRODIGY_CS_05.git

cd packet-sniffer

Install the dependencies:

pip install scapy

Windows users: Ensure WinPcap is installed for packet capturing (e.g., use npcap).

Usage
For Windows Users: You need to install WinPcap or Npcap for packet capturing.

For Linux Users: No additional installation is required; you can run the tool directly.

Run the packet sniffer using: sudo python3 packet_sniffer.py

The tool will capture and display a specified number of packets, showing the following details:

Source IP Address

Destination IP Address

Protocol (TCP, UDP, ICMP)

Payload Data

Example Output
Packet captured:

Source IP: 192.168.1.10

Destination IP: 192.168.1.1

Protocol: TCP

Payload:

Ethical Considerations
This tool is intended for educational purposes only. Always ensure you have permission before capturing network traffic on any network. Use this tool responsibly and ethically.

This project was developed as part of a virtual internship at Prodigy InfoTech.

License
This project is licensed under the MIT License - see the LICENSE file for details.
