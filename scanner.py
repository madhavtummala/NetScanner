import os
import socket
import progressbar

BASE_IP = socket.gethostbyname(socket.gethostname())
BASE_IP = BASE_IP[:BASE_IP.rfind(".")] + "."

bar = progressbar.ProgressBar(maxval=256, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

bar.start()
for i in range(256):
	IP = BASE_IP+str(i)
	bar.update(i)
	response = os.system("fping -c1 -t10 " + IP + " > /dev/null 2>&1")
	if response == 0:
		print (IP)
bar.finish()