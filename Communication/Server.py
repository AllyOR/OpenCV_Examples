import socket

# port for our server.
port = 5000

# We create a socket object for the server.
s = socket.socket()          
print("Server started")
  
# The server listen the requests from other computers on the network.
s.bind(('', port))         
print("Port of the server %s" %(port))
  
# put the socket into listening mode.
s.listen(5)      
print("Server listening..")
  
while True: 
  
   # Wait for connection with a client. 
   c, addr = s.accept()      
   print('Conected client', addr)
   
   # Read the message from the client.
   print(c.recv(1024))
   
   # send a message to the client.  
   c.sendall(b'Hello world from the server!')
  
   # Close the socket (connection with the client)
   c.close()
   print("Client desconected")
