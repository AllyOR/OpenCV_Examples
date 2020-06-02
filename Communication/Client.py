import socket                
  
#Host of the server
host = "127.0.0.1"

# Define the port of the server, on which you want to connect 
port = 5000

# Create a socket object 
s = socket.socket()          

# connect to the server  
s.connect((host, port))

# send a message to the server.  
s.sendall(b'Hello world from the client!')

# receive the messages from the server 
print(s.recv(1024))
   
# close the connection 
s.close()  
