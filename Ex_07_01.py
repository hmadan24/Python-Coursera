# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
file = fh.read()
print(file.upper())
