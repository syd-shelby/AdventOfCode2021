#vars --arrays for binary counts are represented from left to right
len = 12
zeros = [0] * len
ones = [0] * len
gamma = [0] * len
epsilon = [0] * len

#open file
f = open('input.txt', 'r')

#find counts of binary numbers in each place
while(True):
	line = f.readline()
	if not line:
		break
		
	for i in range(len): #number of chars in each binary number
		if int(line[i]) == 0:
			zeros[i] += 1
		elif int(line[i]) == 1:
			ones[i] += 1			

#create gamma and epsilon as arrays
for i in range(len): #this could all be done better with just math
	if zeros[i] > ones[i]:
		gamma[i] = 0
		epsilon[i] = 1
	else:
		gamma[i] = 1
		epsilon[i] = 0


#convert gamma and epsilon into decimal numbers
g = 0
e = 0
for i in range(len):
	g += pow(2, len-i-1)*gamma[i]
	e += pow(2, len-i-1)*epsilon[i]

#answer
print g*e
