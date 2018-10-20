# 10.2 Data Structures - Tuples
#
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
#
# Input File:
# mbox-short.txt

fname = input("Enter file:")
if len(fname) < 1 :
    fname = "clown.txt"
hand = open(fname)

di = dict()
for lin in hand:
    #lin = lin.rstrip()
    wds = lin.split()

    for w in wds:
        di[w] = di.get(w,0) + 1

print(di)

tmp = list()
for k,v in di.items() :
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)
print('Sorted', tmp[2 :5])
for v,k in tmp[:5] :
    print(k,v)
