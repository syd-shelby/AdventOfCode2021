#testing out solutions with better runtime based on internet research

#get an array of fish read in
f = open('input.txt', 'r')
line = f.readline()
nums = map(int,line.split(','))

#create bins and init wit start data
bin = [0]*9
for n in nums:
	bin[n] += 1

for day in range(256):
	reset = bin[0]
	bin[0] = bin[1]
	bin[1] = bin[2]
	bin[2] = bin[3]
	bin[3] = bin[4]
	bin[4] = bin[5]
	bin[5] = bin[6]
	bin[6] = bin[7]+reset
	bin[7] = bin[8]
	bin[8] = reset


print sum(i for i in bin)
