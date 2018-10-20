# Playground

# Sample data:
# http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)

# Actual data:
# http://py4e-data.dr-chuck.net/comments_51637.json (Sum ends with 93)

import urllib.request, urllib.parse, urllib.error
import json

count = 0

while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    print('Retrieving', url)
    data = urllib.request.urlopen(url)
    rsult = data.read()
    info = json.loads(rsult)
    print('Retrieved', len(info), 'characters')

    corral = info.get('comments')

    for item in corral:
        count = count + item["count"]
    print(count)


# Written Instruction
# 1. prompt for a URL
# 2. read the JSON data from that URL using urllib
# 3. parse and extract the comment counts from the JSON data
# 4. compute the sum of the numbers in the file
