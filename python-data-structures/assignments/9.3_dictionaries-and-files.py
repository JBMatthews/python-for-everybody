# 9.3 - Lecture Code

# ---wordcount---
# counts = dict()
# print('Enter a line of text:')
# line = input('')
#
# words = line.split()
#
# print('Words:', words)
#
# print('Counting...')
# for word in words:
#   counts[word] = counts.get(word,0) + 1
# print('Counts', counts)
#-----------------


# ---iteration---
# counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
# for key in counts:
#     print(key, counts[key])
#-----------------


# Histogram - counts word occurrences
#
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
