import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]
'''

info = json.loads(data)
print(f"User counts: len(info)")

for item in info:
    print(f"Name: {item['name']}")
    print(f"Id: {item['id']}")
    print(f"Attr: {item['x']}")