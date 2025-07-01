# open inputFile.txt with the intention of reading it
inputFile = open("inputFile.txt", "r")

# open passFile.txt with the intention of writing it
passfile = open("passFile.txt", 'w')

# open failFile.txt with the intention of writing it
failfile = open("failFile.txt", 'w')

# loop through each line in inputFile.txt
for line in inputFile:
    words = line.split()
    if (words[2] == "P"):
        passfile.write(line)
    else:
        failfile.write(line)

# close inputFile.txt
inputFile.close()

# close passFile.txt
passfile.close()

# close failFile.txt
failfile.close()