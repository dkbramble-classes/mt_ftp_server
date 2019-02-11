from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket
import ipaddress

ipaddress.ip_address('192.168.0.1')

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/Users/lbassett", perm="elradfmw")
authorizer.add_anonymous("/Users/lbassett", perm="elradfmw") #Make direcory the home direcory of the host machine (which can be navigated by ftp.cwd)

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "You have connected sucessfully!"

IP = input("Please Enter the IP address you want as server: ")
print(IP)
server = FTPServer((IP, 1026), handler) #Make IP the IP of the host machine

server.serve_forever()