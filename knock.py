#!/usr/bin/env python
"""knock.py: A simple portscan, still without host scan and threading"""

__author__ = "GilsonJr"
__version__ = "1.0"
__status__ = "Development"

from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from pyfiglet import figlet_format

banner = figlet_format('Knock!', font='5lineoblique')
print(banner)

ip = input('IP: ')
range = input('port range (port-port): ')
initial_port = int(range.split('-')[0])
final_port = int(range.split('-')[1])
while 1:
    proto = input('TCP(1)/UDP(2): ')
    if proto == '1':
        s = socket(AF_INET, SOCK_STREAM)
        break
    elif proto == '2':
        s = socket(AF_INET, SOCK_DGRAM)
        break
    else:
        print('Invalid entry')
        continue
while initial_port != final_port + 1:
    if s.connect_ex((ip, initial_port)) == 0:
        s.close()
        print(f'Port {initial_port} open')
    else:
        pass
    initial_port += 1
