import urllib.parse, urllib.request
import json, ssl

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# ignore ssl certificate errors
utx = ssl.create_default_context()
utx.check_hostname = False
utx.verify_mode = ssl.CERT_NONE 

while True:
    location = input("Enter the location: ")
    if len(location) < 1:
        break

    location = location.strip()
    params = dict()
    params['q'] = location

    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=utx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    js = json.loads(data)
    
    if not js or 'features' not in js:
        print('=== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('=== Object not found ===')
        print(data)
        break

    # print(json.dumps(js,  indent=4))
    pc = js['features'][0]['properties']['plus_code']
    print('Plus code', pc)

