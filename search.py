file = input("Enter the name of the file: ")
try:
    fhandle = open(file)
except:
    print("Invalid file name")
    quit()

count = 0;
sum = 0;
for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count += 1
    
    i = line.find(':')
    n = float(line[(i+1):].strip())
    sum += n

average = sum/count
print(f"Average spam confidence: {average}")
