import xml.etree.ElementTree as ET
import urllib.request

url = input('Enter the url location for xml: ')
if (len(url) < 1):
    # sample url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    url = 'http://py4e-data.dr-chuck.net/comments_2057926.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()

for result in counts:
    # print(result.text)
    n = int(result.text)
    nums.append(n)
print('Count:', len(nums))
print('Sum:', sum(nums))