#vars --arrays for binary counts are represented from left to right
length = 12
lines = []

#open file
f = open('input.txt', 'r')

#read in lines
while(True):
	line = f.readline()
	if not line:
		break
			
	lines.append(line)


#start filtering down list. could be done more simply with recursion but lazy
ogr_list = list(lines)
pos = 0
while(True):
	if len(ogr_list) == 1:
		break
	
	#recalculate ones and zeros every time. Terrible big O
	zeros = [0] * length
	ones = [0] * length
	
	for ogr in ogr_list:
		for i in range(length): #number of chars in each binary number
			if int(ogr[i]) == 0:
				zeros[i] += 1
			elif int(ogr[i]) == 1:
				ones[i] += 1			


	#filter based on criteria - making this faster could move the above loop out and adjusting vals based on what is removed
	pop_list = []
	criteria = '1' if zeros[pos] <= ones[pos] else '0'
	for i in range(len(ogr_list)):
		if ogr_list[i][pos] != criteria:
			pop_list.append(ogr_list[i])
	for p in pop_list:
		ogr_list.remove(p)
	pos += 1

#should be a function but just copying, pasting, and modifying apove for co2 scrubber rating
csr_list = list(lines)
pos = 0
while(True):
        if len(csr_list) == 1:
                break

        #recalculate ones and zeros every time. Terrible big O
        zeros = [0] * length
        ones = [0] * length

        for csr in csr_list:
                for i in range(length): #number of chars in each binary number
                        if int(csr[i]) == 0:
                                zeros[i] += 1
                        elif int(csr[i]) == 1:
                                ones[i] += 1


        #filter based on criteria - making this faster could move the above loop out and adjusting vals based on what is removed
        pop_list = []
        criteria = '1' if zeros[pos] > ones[pos] else '0'
        for i in range(len(csr_list)):
                if csr_list[i][pos] != criteria:
                        pop_list.append(csr_list[i])
        for p in pop_list:
                csr_list.remove(p)
        pos += 1

#convert vals to ints
ogr = ogr_list[0]
csr = csr_list[0]
o = 0
c = 0
for i in range(length):
	o += pow(2, length-i-1)*int(ogr[i])
	c += pow(2, length-i-1)*int(csr[i])

#answer
print o*c
