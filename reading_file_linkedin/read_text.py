inputfile = open('inputFile.txt', 'r')
count = 0
for line in inputfile:
    words = line.split()
    if (words[2] == "P"):
        count += 1
        print(line, end='')
inputfile.close()
print(f"Total number of people who passed are: {count}")