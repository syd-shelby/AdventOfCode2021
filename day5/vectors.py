max = 1000
grid = [[0 for j in xrange(max)]  for i in xrange(max)]

x1s = []
y1s = []
x2s = []
y2s = []

#read in lines
f = open('input.txt' , 'r')
while(True):
	line = f.readline().replace(",", " ").replace("-", "").replace("> ", "")
	if not line:
		break
	nums = line.split()
	x1s.append(int(nums[0]))
	y1s.append(int(nums[1]))
	x2s.append(int(nums[2]))
	y2s.append(int(nums[3]))

#draw out lines
for i in range(len(x1s)):
	#hoizontal
	if x1s[i] == x2s[i]:
		for y in range(y1s[i] , y2s[i]+1 if y1s[i] < y2s[i] else y2s[i]-1, 1 if y1s[i] < y2s[i] else -1):
			grid[ x1s[i] ][y] += 1	
	#vertical
	elif y1s[i] == y2s[i]:
		for x in range(x1s[i],  x2s[i]+1 if x1s[i] < x2s[i] else x2s[i]-1, 1 if x1s[i] < x2s[i] else -1):
			grid[x][y1s[i]] += 1	

	#diagnol 45 degrees
	else:
		y = y1s[i]
		dir = 1 if y1s[i] < y2s[i] else -1
		for x in range(x1s[i],  x2s[i]+1 if x1s[i] < x2s[i] else x2s[i]-1, 1 if x1s[i] < x2s[i] else -1):
                        grid[x][y] += 1	
			y += dir

#print grid (for debugging. Will be commented out
#for x in range(max):
#	for y in range(max):
#		if not grid[y][x]:	
#			print '.',
#		else:
#			print grid[y][x], #flipping so coordinate system and row cols make sense
#	print

overlap = 0

#find answer
for x in range(max):
        for y in range(max):
		if grid[x][y] >= 2:
			overlap += 1

print overlap
