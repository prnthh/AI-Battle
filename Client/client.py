import socket

s = socket.socket()
host = socket.gethostname()
print ("Choose a port to connect to")

port=int(input(">"))
print ("Attempting to connect to port ",port)
a = 1
s.connect((host, port))
while True:
	print(s.recv(1024))
	a = a+1
	s.send(bytes("done lol %s" %a, "utf-8"))
s.close