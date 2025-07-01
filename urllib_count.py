import urllib.request, urllib.parse, urllib.error

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}
for line in fhandle:
    words = line.decode().split()
    for w in words:
        counts[w] = counts.get(w, 0) + 1

print(counts)