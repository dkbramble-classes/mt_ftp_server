#current ideas from https://www.techinfected.net/2017/07/create-simple-ftp-server-client-in-python.html
import sys
import os
import socket
from ftplib import FTP

def usage_error(cmd):
    if cmd != '':
        print("improper usage of '" + cmd + "\'")
    print("Commands: \n\t CONNECT <server name/IP address> <server port> \n\t LIST \n\t RETRIEVE <filename> \n\t STORE <filename> \n\t QUIT")

quit = False
connect = False
ftp = FTP('')
while quit == False:
    command = input("Enter a command: ") #ask for input
    os.system('cls' if os.name == 'nt' else 'clear')
    function = command.split(" ", 3) #splice the input into a list delimited by spaces
    if connect == False:
        if function[0].upper() == "CONNECT":
            if len(function) == 3: # if the right number of parameters
                response = os.system("ping -c 1 " + function[1]) #ping the server to see if it's on the network
                if response == 0: #if ping successful
                    ftp.connect(function[1],int(function[2]))
                    ftp.login()
                    ftp.cwd('/Documents') #replace with your directory
                    ftp.retrlines('LIST')
                    connect = True
                    print("connected to " + function[1])
                else:
                    print("IP address / Host name not valid, please try again")
            else:
                usage_error(function[0])
        elif function[0].upper() == "QUIT":
            quit = True
        else:
            print("Need to connect to the server first!")
            print("Usage: CONNECT <server name/IP address> <server port>")
    else:
        if function[0].upper() == "RETRIEVE":
            if len(function) == 2:
                print(function[1])
            else:
                usage_error(function[0])
        elif function[0].upper() == "STORE":
            if len(function) == 2:
                print(function[1])
            else:
                usage_error(function[0])
        elif function[0].upper() == "LIST":
            print("list")
        elif function[0].upper() == "QUIT":
            ftp.close()
            quit = True
        else:
            usage_error(function[0])
print("Goodbye")
