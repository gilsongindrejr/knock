#!/usr/bin/python3
"""knock.py: A simple portscan, still without host scan and threading"""

__author__ = "GilsonJr"
__version__ = "1.0"
__status__ = "Development"

from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import pyfiglet
import argparse

banner = pyfiglet.figlet_format('Knock!', font='5lineoblique')


parser = argparse.ArgumentParser(prog='Knock', usage='\nknock -ip <ip address> -p <port-port> --proto <TCP/UDP>', description='Simple portscan')
parser.add_argument('-ip', help='IP address', type=str, required=True)
parser.add_argument('-p', help='Port range (port-port)', type=str, required=True)
parser.add_argument('--proto', help='Protocol (TCP/UDP)', type=str, required=True)
args = parser.parse_args()

def port_knocker(ip, ports, proto):
    print(banner)
    print(__version__)
    print()
    initial_port = int(ports.split('-')[0])
    final_port = int(ports.split('-')[1])
    while 1:
        if proto == 'TCP':
            s = socket(AF_INET, SOCK_STREAM)
            break
        elif proto == 'UDP':
            s = socket(AF_INET, SOCK_DGRAM)
            break
        else:
            print('Invalid protocol')
            break
    while initial_port != final_port + 1:
        if s.connect_ex((ip, initial_port)) == 0:
            s.close()
            print(f'Port {initial_port} open')
        else:
            pass
        initial_port += 1


if __name__ == '__main__':
    port_knocker(ip=args.ip, ports=args.p, proto=args.proto)
