#!/usr/bin/python3
"""knock.py: A simple portscan"""

__author__ = "GilsonJr"
__version__ = "2.3"
__status__ = "Development"

from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from pyfiglet import figlet_format
import argparse
from re import search
from colorama import Fore

banner = figlet_format('Knock!', font='5lineoblique')

parser = argparse.ArgumentParser(
    prog='Knock',
    usage='knock -ip <IP ADDRESS> -p <PORT-PORT> --proto <TCP/UDP>',
    description='Scan for open ports on target IP.'
)

parser.add_argument('-ip', help='IP address', type=str, required=True)
parser.add_argument('-p', help='Port range (port-port)', type=str, required=True)
parser.add_argument('--proto', help='Protocol (TCP/UDP)', type=str, required=True)
args = parser.parse_args()


def print_banner():
    print(banner)
    print(__version__)
    print()


def port_knocker(ip, ports, proto):
    # Get ports number
    try:
        initial_port = int(ports.split('-')[0])
        final_port = int(ports.split('-')[1])
    except Exception:
        print(Fore.RED + 'Invalid port')
        return 0

    # Check if ports and proto is valid
    if initial_port > final_port:
        print(Fore.RED + 'Initial port must be lower than final port')
        return 0
    else:
        if proto == 'TCP':
            s = socket(AF_INET, SOCK_STREAM)
        elif proto == 'UDP':
            s = socket(AF_INET, SOCK_DGRAM)
        else:
            print(Fore.RED + 'Invalid protocol')
            return 0

    # Regex the ip and try the connection with informed ip address
    try:
        ip_addr = search('[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}', ip).string
        s.connect_ex((ip_addr, initial_port)) == 0
    except Exception:
        print(Fore.RED + 'Invalid IP address')
        return 0

    # loop knocking all doors
    while initial_port != final_port + 1:
        if s.connect_ex((ip_addr, initial_port)) == 0:
            s.close()
            print(f'Port {initial_port} open')
        else:
            pass
        initial_port += 1


if __name__ == '__main__':
    print_banner()
    port_knocker(ip=args.ip, ports=args.p, proto=args.proto)
