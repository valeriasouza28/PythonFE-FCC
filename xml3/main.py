import xml.etree.ElementTree as ET

input = '''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Brent</name>
</user>
</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User cont:', len(lst))

lst2 = stuff.findall('user')
print('User count:', len(lst2))