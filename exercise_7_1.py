#use words,txt as the file name and prints the contents of the file in the upper case
fname = input("Enter the file name:")
fh = open(fname)
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())