f = open('depths.txt','r')
count = 0
one = int(f.readline())
two = int(f.readline())
three = int(f.readline())
oldsum = one+two+three
one = two
two = three
three = int(f.readline())
newsum = one+two+three
while (True):
	if (newsum > oldsum):
		count = count+1
	one = two
	two = three
	threeprime = f.readline()
	if not threeprime:
		break
	three = int(threeprime)
	oldsum = newsum
	newsum =one+two+three
print count
f.close()
