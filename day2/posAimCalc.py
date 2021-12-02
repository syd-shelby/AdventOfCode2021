#define vars
depth = 0
horiz = 0
aim = 0

#read lines and break up
f = open('directions.txt', 'r')
while (True):
	line = f.readline().split()
	if not line:
		break

	dir = line[0]
	val = int(line[1]) #lmao at my lack of error checking
	
	#update vars
	if dir == "forward":
		horiz = horiz + val
		depth = depth + (aim * val)
	elif dir == "down":
		aim  = aim + val
	elif dir == "up":
		aim = aim - val

f.close()

#multiple
print depth*horiz
