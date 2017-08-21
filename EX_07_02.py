# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total_confidence = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    temp_num = line[line.find(':')+1:]
    temp_num = float(temp_num)
    total_confidence = total_confidence + temp_num
    count = count + 1
print("Average spam confidence:", total_confidence/count)