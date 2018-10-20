# 8.3 Data Structures
#
# Code from the lecture
#

# # First Example
# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
#
# for w in stuff:
#     print(w)

# Second Example - How to Parse Email Data
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From') : continue
    words = line.split()
    print(words[2])
