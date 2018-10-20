# # Tuples and Dictionaries
# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
#
# for (k,v) in d.items():
#     print(k, v)
#
# tups = d.items()
# print(tups)

# # Using sorted()
# d = {'a':10, 'b':1, 'c':22}
# t = sorted(d.items())
#
# for k, v in sorted(d.items()):
#     print(k, v)
#
# print(d.items())

# # Sort by Values Instead of Key
# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k, v in c.items():
#     tmp.append( (v, k) )
# print(tmp)
#
# tmp = sorted(tmp, reverse=True)
# print(tmp)

# "Unknown" from previous code
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)
