from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/Users/lbassett", perm="elradfmw")
authorizer.add_anonymous("/Users/lbassett", perm="elradfmw") #Make direcory the home direcory of the host machine (which can be navigated by ftp.cwd)

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "You have connected sucessfully!"

IP = input("Please Enter the IP address you want as server: ")
print(IP)
server = ThreadedFTPServer((IP, 1026), handler) #Make IP the IP of the host machine

server.serve_forever()