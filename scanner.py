import os
import socket

BASE_IP = socket.gethostbyname(socket.gethostname())
BASE_IP = BASE_IP[:BASE_IP.rfind(".")] + "."

for i in tqdm.tqdm(range(256)):
	IP = BASE_IP+str(i)
	response = os.system("fping -c1 -t10 " + IP + " > /dev/null 2>&1")
	if response == 0:
		print (IP)