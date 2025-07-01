import re

while(True):
    file = input("Enter the file: ")
    if (len(file) < 1):
        continue
    break
num = []
fhandle = open(file)
for line in fhandle:
    line = line.strip()
    n = re.findall('[0-9]+', line)
    if (len(n) > 0):
        for i in n:
            no = int(i)
            num.append(no)
print(f'The sum of all numbers appearing in the file is {sum(num)}.')
