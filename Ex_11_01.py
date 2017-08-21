# Extract numbers from file and sum them

fname = input('Enter the file name:')
fhandle = open(fname)
#nums = list()
import re

#for line in fhandle:
#	x = re.findall('[0-9]+',line)
#	for i in x:
#		nums.append(float(i))

#print(len(nums), sum(nums))

print(sum([float(x) for x in re.findall('[0-9]+',fhandle.read())]))