import os
import time

while True :
	os.system("git add cifar10.pth")
	os.system("git commit -m \"M\"")
	os.system("git push -u origin master")
	time.sleep(100)