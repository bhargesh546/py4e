while (True):
    file = input("Enter the name of the file: ")
    if (len(file) < 1):
        continue
    break
fhandle = open(file)

words_dict = {}
for line in fhandle:
    if (len(line) < 1):
        continue
    words = line.strip().split()
    for w in words:
        if (len(w) < 1):
            continue
        words_dict[w] = words_dict.get(w, 0) + 1

highest = None
word = None
for k,v in words_dict.items():
    if (highest == None or v > highest):
        highest = v
        word = k
print(word, words_dict[word])