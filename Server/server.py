import socket, subprocess, time

print ("#This is the server application for Robattle.")
print ("#Initializing game setup.")
#print ("#Enter desired grid size")
#gridSize = int(input(">"))
gridSize = 10
grid = [
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,"X",0,0,0,0,0,0,"Y",0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],]

p1Health=100
p2Health=100

def move(pid, dir):
	for i in range(len(grid)):
		for j in range(len(grid)):
			if(grid[i][j]==pid):
				x=i
				y=j

	if(dir=="up"):
		grid[x-1][y]=grid[x][y]
		grid[x][y]=0
	elif(dir=="down"):
		grid[x+1][y]=grid[x][y]
		grid[x][y]=0
	elif(dir=="left"):
		grid[x][y-1]=grid[x][y]
		grid[x][y]=0
	elif(dir=="right"):
		grid[x][y+1]=grid[x][y]
		grid[x][y]=0


def execAction(action, pid):
	action = action.split()
	if(action[0]=="ping"):
		return "pong"
	elif(action[0]=="move"):
		if(action[1]=="up"):
			move(pid, "up")
		if(action[1]=="down"):
			move(pid, "down")
		if(action[1]=="left"):
			move(pid, "left")
		if(action[1]=="right"):
			move(pid, "right")
		return "moved"

def round():
	c.send(bytes("There should be a grid here", "utf-8"))
	print("Received message from p1:", c.recv(1024))
	print("\n"*5)
	displayGrid()
	time.sleep(2)

	c2.send(bytes("There should be a second grid here", "utf-8"))
	print("Received message from p2:", c2.recv(1024))
	print("\n"*5)
	displayGrid()
	time.sleep(2)


def displayGrid():
	for i in range(gridSize-1):
		for j in range(gridSize):
			print (grid[i][j], end="")
		print()

		#^ print out grid values v print out separator lines
"""		for j in range(gridSize*2):
					print ("_", end="")
		print()"""

"""
############################################################
#this is where the two game clients connect to the server
host = socket.gethostname()
port1 = 9090
port2 = 9091
s1 = socket.socket()
s1.bind((host, port1))

s2 = socket.socket()
s2.bind((host, port2))


s1.listen(5)
s2.listen(5)

c, addr = s1.accept()
print ("#got connection from", addr)
c2, addr2 = s2.accept()
print ("#got connection from", addr2)

round()
round()
round()
round()

c.close()
c2.close()
############################################################
"""

