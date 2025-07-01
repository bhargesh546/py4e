import json, urllib.request, urllib.parse, urllib.error
import getpass, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
api_key = getpass.getpass('Enter the api key: ')

while True:
    address = input('Enter the location: ')
    if (len(address) < 1):
        break
    params = {'address': address.strip(), 'key': api_key}
    url = serviceurl + urllib.parse.urlencode(params)

    print(f"Retrieving url: {url}")
    
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print(f"Retrieved {len(data)} characters")

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print("====Failure to retrieve====")
        print(data)
        break

    print(json.dumps(js, indent=4))
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    long = js["results"][0]["geometry"]["location"]["lng"]
    print(f"Latitude: {lat}")
    print(f"Longitude: {long}")
    
    location = js["results"][0]["formatted_address"]
    print(location)
    break
    