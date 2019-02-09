#current ideas from https://www.techinfected.net/2017/07/create-simple-ftp-server-client-in-python.html
import sys

quit = False
connect = False
while quit == False:
    command = input("Enter a command: ") #ask for input
    function = command.split(' ', 3) #splice the input into a list delimited by spaces
    if connect == False:
        if function[0].upper() == "CONNECT":
            connect = True
            print("connected")
        elif function[0].upper() == "QUIT":
            quit = True
        else:
            print("Need to connect to the server first!")
    else:
        if function[0].upper() == "RETRIEVE":
            print(function[1]) #Retrieves 1st argument (NEED TO CHECK IF NULL)
        elif function[0].upper() == "STORE":
            print("store")
        elif function[0].upper() == "LIST":
            print("list")
        elif function[0].upper() == "QUIT":
            quit = True
        else:
            print("Not a command, please try again")
print("Goodbye")
