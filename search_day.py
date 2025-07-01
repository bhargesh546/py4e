while(True):
    file = input("Enter the name of the file: ")
    if (len(file) < 1):
        continue
    break
fhandle = open(file)

count = 0
for line in fhandle:
    if not line.startswith('From'):
        continue
    words = line.strip().split()
    if (len(words) < 3):
        continue
    print(words[2])
    count += 1

print(f"There were {count} line in the file with From as the first word")