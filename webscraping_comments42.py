from bs4 import BeautifulSoup
import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

numbers = []
tags = soup('span')
for tag in tags:
    print(f"Tags: {tag}")
    numbers.append(int(tag.contents[0]))
    #print(f"The numbers are: {tag.contents[0]}")

print(f"Sum = {sum(numbers)}")