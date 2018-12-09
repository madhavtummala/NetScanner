import os
import socket
import tqdm

BASE_IP = socket.gethostbyname(socket.gethostname())
BASE_IP = BASE_IP[:BASE_IP.rfind(".")] + "."

my_list = []

for i in tqdm.tqdm(range(256)):
	IP = BASE_IP+str(i)
	response = os.system("fping -c1 -t10 " + IP + " > /dev/null 2>&1")
	if response == 0:
		my_list.append(IP)

for i in my_list:
	print(i)