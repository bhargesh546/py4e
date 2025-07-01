import xml.etree.ElementTree as ET

data = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>
'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
print(f"The users lists is of length: {len(lst)}")

for item in lst:
    print(f"Name: {item.find('name').text}")
    print(f"ID: {item.find('id').text}")
    print(f"Attribute: {item.get('x')}")
 