import urllib.request
import json

url = input('Enter the url location for json file: ')
if (len(url) < 1):
    # sample url = 'http://py4e-data.dr-chuck.net/comments_42.json'
    url = 'http://py4e-data.dr-chuck.net/comments_2057927.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

print("Retrieved", len(data), "characters")

js = json.loads(data)

nums = list()

for i in js['comments']:
    n = i['count']
    nums.append(n)

print(len(nums))
print(sum(nums))
