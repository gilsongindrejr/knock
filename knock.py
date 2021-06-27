#!/usr/bin/env python
"""knock.py: Um simples port scan, ainda sem scan de host e treading"""

__author__ = "GilsonJr"
__version__ = "1.0"
__status__ = "Desenvolvimento"

from socket import *
import pyfiglet

banner = pyfiglet.figlet_format('Knock!', font='5lineoblique')
print(banner)

ip = input('IP: ')
range = input('Portas (porta-porta): ')
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
        print('Entrada inválida')
        continue
while initial_port != final_port + 1:
    if s.connect_ex((ip, initial_port)) == 0:
        s.close()
        print(f'Porta {initial_port} aberta')
    else:
        pass
    initial_port += 1
