fname = input('Enter the name of the file: ')
if (len(fname) < 1):
    fname = 'mbox-short.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    print(pieces)