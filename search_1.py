file = input("Enter the name of the file: ")

try:
    fhandle = open(file)
except:
    print("Invalid file name")
    quit()
count = 0
for line in fhandle:
    if line.startswith("From:"):
        print(line.strip())
        count += 1

print(f"Number of senders found: {count}")