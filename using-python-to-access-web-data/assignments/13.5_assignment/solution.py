# Final Code

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

count = 0
sum = 0

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving', address)
    url = urllib.request.urlopen(address)
    data = url.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    stuff = tree.findall('comments/comment')
    for thing in stuff:
        count = count + 1
        sum = sum + int(thing.find('count').text)
    print("Count: ", count)
    print("Sum: ", sum)
