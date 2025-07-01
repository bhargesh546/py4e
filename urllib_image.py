import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhandle = open('cover.jpg', 'wb')

size = 0
while True:
    info = img.read(10000)
    if (len(info) < 1):
        break
    size += len(info)
    fhandle.write(info)

print(f'Number of characters in the file is: {size}')
fhandle.close()
