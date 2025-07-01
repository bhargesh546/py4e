while(True):
    file = input("Enter the file name: ")
    if (len(file) < 1):
        continue
    break

fhandle = open(file)

hour = {}
for line in fhandle:
    if not line.startswith('From ') or len(line) < 1:
        continue
    words = line.strip().split()
    time = words[5].strip().split(':')
    hr = time[0]
    hour[hr] = hour.get(hr, 0) + 1

tmp = [(t,c) for t,c in hour.items()]

tmp.sort()
for t,c in tmp:
    print(t, c)