# mt_ftp_server
CIS 457 Project 1: Multi-Threading FTP Server

The server program binds to a port and listens for requests from a client. After a client connects to the server, the server waits for commands. When the client sends a terminate message (quit), the server terminates the connection and waits for the next connection.

How to Run:

This program requires that you first start the server (ftp_server.py), then start the client (ftp_client.py). Download all the files from this Github to ensure you have all dependencies.

Server:

To start, run the executable "ftp_server" by double clicking on the file. This will open a window in the terminal prompting for an ip/hostname to host the server (preferrably your own). 
  
Client:

To start, run the executable "ftp_client" by double clicking on the file. This will open a window asking in terminal. The usage for the client is as follows:

1.	CONNECT <server name/IP address> <server port>: This command allows a client to connect to a server. The arguments are the IP address of the server and the port number on which the server is listening for connections. For you, this will be the ip/hostname inputted on the server

2.	LIST: When this command is sent to the server, the server returns a list of the files in the current directory on which it is executing. The client should get the list and display it on the screen.

3.	RETRIEVE <filename>: This command allows a client to get a file specified by its filename from the server.

4.	STORE <filename>: This command allows a client to send a file specified by its filename to the server.

5.	QUIT: This command allows a client to terminate the control connection. On receiving this command, the client should send it to the server and terminate the connection. When the ftp_server receives the quit command it should close its end of the connection.
