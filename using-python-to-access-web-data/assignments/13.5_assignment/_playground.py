# Playground

# START LECTURE EXAMPLES

# 13.4 Parsing XML
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes">
     someone@nowhere.com
    </email>
</person>
'''

tree = ET.fromstring(data)
print(tree.find('phone').text)
print(tree.find('email').get('hide'))

print(tree)
# END LECTURE EXAMPLES
