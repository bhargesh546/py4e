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

tmp = [(v,k) for k,v in words_dict.items()]

tmp = sorted(tmp, reverse=True)

for k,v in tmp[:10]:
    print(v, k)