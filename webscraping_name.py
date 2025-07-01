from bs4 import BeautifulSoup
import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


link = input("Enter the url: ")
pos = int(input("Enter the position: "))
count = int(input("Enter the count: "))
n = 0

ln = link.split('/')
wrd = ln[-1]
first_name = wrd.split('_')[-1].split('.')[0]

name_list = []
name_list.append(first_name)

while (n < count):
    url = link
    html = urllib.request.urlopen(url, context=ctx)
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    names = [tag.contents[0] for tag in tags]
    name_list.append(names[pos - 1])
    n += 1
    link = tags[pos - 1].get('href', None)
    if (url == None):
        break

print(' '.join(name_list))
