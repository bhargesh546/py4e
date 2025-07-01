import xml.etree.ElementTree as ET
data = '''
<person>
  <name>Bhargesh</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print(f"Name of the person is: {tree.find('name').text}")
print(f"The Attr is: {tree.find('email').get('hide')}")
