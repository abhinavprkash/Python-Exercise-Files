# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
flot_total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    ipos = line.find(':')
    flot = float(line[ipos + 1:])
    flot_total = flot_total + flot
    count = count + 1
print('Average spam confidence:', flot_total/count)
