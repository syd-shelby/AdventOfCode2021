#get an array of crabs read in
f = open('input.txt', 'r')
line = f.readline()
nums = map(int,line.split(','))
f.close()

#find min and max
max = max(nums)
min = min(nums)

minfuel = -1
pos = 0

for x in range(min, max+1):
	fuel = 0
	for n in nums:
		steps = abs(n-x)
		fuel += steps*(steps+1)/2
	if minfuel == -1 or fuel < minfuel:
		minfuel = fuel
		pos = x


print minfuel, "fuel required for position: ", pos
