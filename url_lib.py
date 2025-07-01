import urllib.request, urllib.parse, urllib.error

# fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
fhandle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')


for line in fhandle:
    print(line.decode().strip())
