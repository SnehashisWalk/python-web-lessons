import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chi</name>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
