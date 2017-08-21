#Creates histogram of email ids and respective count
fname = input('Please enter file name:')
fhandle = open(fname)
email = list()
counts = dict()

for line in fhandle:
	if line.startswith('From '):
		words = line.split()
		email.append(words[1])

for word in email:
	counts[word] = counts.get(word,0) + 1

bigger_value = None
bigger_email = None

for k,v in counts.items():
	if bigger_value == None or v > bigger_value:
		bigger_value = v
		bigger_email = k

print(bigger_email, bigger_value)