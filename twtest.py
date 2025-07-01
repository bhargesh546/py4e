import urllib.request
from twurl import augment
import ssl

print('* Calling Twitter...')
url = augment('https://api.x.com/1.1/statuses/user_timeline.json',
              {'screen_name': 'BhargeshPatel12', 'count': '2'})
print(url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

print ('======================================')
headers = dict(connection.getheaders())
print(headers)