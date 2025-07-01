while (True):
    file = input("Enter the name of the file: ")
    if (len(file) < 1):
        continue
    break
fhandle = open(file)

sender = {}
for line in fhandle:
    if not line.startswith('From '):
        continue
    words = line.strip().split()
    user_link = words[1]
    sender[user_link] = sender.get(user_link, 0) + 1

highest = None
person = None
for k,v in sender.items():
    if (highest == None or v > highest):
        highest = v
        person = k
print(person, sender[person])