From Scapy

import socket
import logging


SYSLOG_SERVER = '192.168.1.100'
SYSLOG_PORT = 514
INTERFACE = 'eth0'
LOG_FILE = 'packet_logs.txt'
FORWARD_TO_SYSLOG = True


#Logging setup locally
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - &(message)s')


#Syslog forwarder
def send_syslog(message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(message, 'utf-8'), (SYSLOG_SERVER, SYSLOG_PORT))
        sock.close()
    except Exception as e:
        print(f"Syslog error: {e}")
        