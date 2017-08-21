#Parse mails to find frequency per hour
fname = input('Enter the file name:')
fhandle = open(fname)
freq = dict()

for line in fhandle:
	if line.startswith('From '):
		words = line.split()
		time = words[5]
		hours = time[:2]
		freq[hours] = freq.get(hours,0) + 1

for k,v in sorted(freq.items()):
	print(k,v)