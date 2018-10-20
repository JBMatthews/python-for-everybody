# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

# The basic outline of this problem is to read the file, look for integers using
# the re.findall(), looking for a regular expression of '[0-9]+' and then converting
# the extracted strings to integers and summing up the integers.

# CODE BELOW:
import re

# Setting counter
counter = 0

# Just press Enter input
fname = input("Enter file:")
if len(fname) < 1 :
    fname = "regex_sum_51632.txt"
hand = open(fname)

# Breakdown and findall
lines = hand.read()
num = re.findall('[0-9]+', lines)

# Loop through and add them up
for n in num:
    count = int(n)
    counter = counter + count
print(counter)
