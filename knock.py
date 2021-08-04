#!/usr/bin/python3
"""knock.py: A simple portscan, still without host scan and threading"""

__author__ = "GilsonJr"
__version__ = "2.2"
__status__ = "Development"

from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import pyfiglet
import argparse
from re import search
from colorama import Fore

banner = pyfiglet.figlet_format('Knock!', font='5lineoblique')


parser = argparse.ArgumentParser(prog='Knock', usage='knock -ip <IP ADDRESS> -p <PORT-PORT> --proto <TCP/UDP>',
                                 description='Scan for open ports on target IP.')
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
    try:
        ip_addr = search('[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}', ip).string
        if initial_port > final_port:
            print(Fore.RED + 'Initial port must be lower than final port')
        else:
            while 1:
                if proto == 'TCP':
                    s = socket(AF_INET, SOCK_STREAM)
                    break
                elif proto == 'UDP':
                    s = socket(AF_INET, SOCK_DGRAM)
                    break
                else:
                    print(Fore.RED + 'Invalid protocol')
                    return 0
            while initial_port != final_port + 1:
                if s.connect_ex((ip_addr, initial_port)) == 0:
                    s.close()
                    print(f'Port {initial_port} open')
                else:
                    pass
                initial_port += 1
    except AttributeError:
        print(Fore.RED + 'Invalid IP address')


if __name__ == '__main__':
    port_knocker(ip=args.ip, ports=args.p, proto=args.proto)
