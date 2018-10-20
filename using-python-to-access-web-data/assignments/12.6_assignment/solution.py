
# DATA
# - Sample data:
# http://py4e-data.dr-chuck.net/comments_42.html

#(Sum=2553)
# - Actual data: http://py4e-data.dr-chuck.net/comments_51634.html (Sum ends with 9)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
justspantags = soup('span')

total = 0
count = 0

for alltags in justspantags:
    count = count + 1
    sum = int(alltags.contents[0])
    total = total + sum

print("Count " + str(count))
print("Sum " + str(total))
