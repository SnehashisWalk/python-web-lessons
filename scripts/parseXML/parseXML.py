import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chi</name>
    <email hide="yes" />
</person>'''

print(type(data))

tree = ET.fromstring(data)
print(tree[0])
print(tree.find('name').text)
print('Name:',tree.find('name').text)
print('Attribute of email:',tree.find('email').get('hide'))
