#get an array of fish read in
f = open('input.txt', 'r')
line = f.readline()
nums = map(int,line.split(','))

for day in range(1, 257): #change 257 to 1 higher than the number of days you wanna calculate
	new = 0
	for i in range(len(nums)):
		if not nums[i]:
			new+=1
			nums[i] = 6
		else:
			nums[i] -= 1

	nums.extend([8]*new)
	print "After ",day," days: ", i #, nums 
	#rempve comment in above line to see full data. Just using this for timing analytics. see github comment for stats

print
print len(nums)
		
#this would be a great lab to teach new CS people the significance of big O
