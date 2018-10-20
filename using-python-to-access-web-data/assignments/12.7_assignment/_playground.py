# ############
# Playground #
# ############

# IMPORTS
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

corral = list()

url = input('Enter - ')
rotations = int(input('Enter Count: '))
pos = int(input('Enter Position: '))

for i in range(rotations):
    print('Retrieving:\n', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        corral.append(tag)
    url = corral[pos - 1].get('href', None)
    del corral[:]



#        allhttp = tag.get('href', None)


# DATA
# http://py4e-data.dr-chuck.net/known_by_Fikret.html

# WORD INSTRUCTION
#
# Enter Initial URL
# Enter Number of times to Repeat (repeat)
# Enter Position Index of URL (pos)
#
# Go to 'url'
# Open URL at 'pos'
# Repeat steps 'repeat' times
# Print the URLs Used
#
#
#
#
#
#
#
#
#
#
