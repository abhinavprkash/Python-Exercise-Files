import xml.etree.ElementTree as ET
data = '''<person>
    <name>Abhinav</name>
    <phone type="intl">
    +91 776 600 6343
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))