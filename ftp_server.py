from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/Users/lbassett", perm="elradfmw")
authorizer.add_anonymous("/Users/lbassett", perm="elradfmw") #Make direcory the home direcory of the host machine (which can be navigated by ftp.cwd)

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "You have connected sucessfully!"

server = FTPServer(("35.40.65.30", 1026), handler) #Make IP the IP of the host machine
server.serve_forever()