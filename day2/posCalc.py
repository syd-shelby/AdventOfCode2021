#define vars
depth = 0
horiz = 0

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
	elif dir == "down":
		depth = depth + val
	elif dir == "up":
		depth = depth - val

f.close()

#multiple
print depth*horiz
