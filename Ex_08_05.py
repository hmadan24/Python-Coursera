#Creates list of email ids and total count
fname = input('Please enter file name:')
fhandle = open(fname)
email = list()

for line in fhandle:
	if line.startswith('From '):
		words = line.split()
		email.append(words[1])

for word in email:
	print(word)

print(len(email))

