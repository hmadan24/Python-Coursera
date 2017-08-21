#Prepares list of unique words in a file

fname = input('Enter the file name:')
fhandle = open(fname)
words = list()

for line in fhandle:
	lis = line.split()
	for word in lis:
		if word not in words:
			words.append(word)

words.sort()
print(words)