file = input("Enter the file: ")
fhandle = open(file)

words = []
for line in fhandle:
    if len(line) == 0:
        continue
    w = line.strip().split()
    for wrds in w:
        if wrds not in words:
            words.append(wrds)

words.sort()
print(words)





