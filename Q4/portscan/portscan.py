##################################################
## Q2 - Assessment Webscrapper Apache Server.
##################################################
## Author: Wagner Ribeiro (L00170338).
## Email: L00170338@student.lyit.ie
## Status: Development.
##################################################

import sys
import socket
from datetime import datetime
   

def scan_target():
	# Defining a target to scan ports.
	target = socket.gethostbyname(sys.argv[1]) 
	print("Scanning Target: " + target)
	print("=" * 50)
	try:
		for port in range(1,65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port))
			if result ==0:
				print("Port {} is open".format(port))
			s.close()
	except socket.error:
			print("\ Server not responding to the quests, check if host is alive.!!!!")
			sys.exit()
	print ("Port Scanning complete")


def main():
	if len(sys.argv) == 2:
		scan_target()
	else:
		print("Invalid Number of Argument")

if __name__ == '__main__':
	main()
