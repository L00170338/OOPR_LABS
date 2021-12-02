import paramiko
from paramiko import SSHClient
import time
import re
import sys


commands = ['hostname', 'ls -al / > longList.txt && ls -l longList.txt ', 'cat longList.txt']
def ssh_connection(ip, port, username, password):
    try:
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), port, username, password)
        connection = session#.invoke_shell()
        for cmd in commands:
            stdin, stdout, stderr  = connection.exec_command(cmd) #unix command to list directory contents and save to file
            time.sleep(1)
            vm_output = stdout.readlines()
            vm_output = ''.join(vm_output)
            
            if  "Invalid input" in vm_output:  
                print("There was at least one IOS syntax error on device {}".format(ip))
                print (vm_output)
            else:
                print("Commands successfully executed on {}".format(ip))
                print (vm_output)
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


def main():
    if len(sys.argv) < 1 or len(sys.argv) >= 3:
        print ("Connecting to SSH with the details inserted:")
        ip = sys.argv[1]
        username = sys.argv[2]
        password = sys.argv[3]
        ssh_connection(ip, "22", username, password )
    else:
        ip = input ("Enter Hostname or IP :")
        username = input ("Enter Username :")
        password = input("Enter Password : ")
        ssh_connection(ip, "22", username, password )

if __name__ == '__main__':
	main()
