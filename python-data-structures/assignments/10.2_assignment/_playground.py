# 10.2 Assignment - testing playground
#
# Input File:
# mbox-short.txt
#
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
#
# GO ON AN TEST BELOW:


# *** Imagine this as an array after you split it

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#[  0,        1                   , 3, 4 , 5,   6    ,  7]
# File Input Section Process
fname = input("Enter file:")
if len(fname) < 1 :
    fname = "mbox-short.txt"
hand = open(fname)

di = dict()

for lin in hand:
    if not lin.startswith("From "):
        continue
    line_words = lin.split()
    time = line_words[5]
    time_data = time.split(':')
    hour = time_data[0]
    di[hour] = di.get(hour, 0) + 1

print(sorted(di.items()))

tmp_lst = list()

for k,v in sorted(di.items()):
    print(k,v)
# tmp = list()
#
# for k,v in di.items() :
#     newt = (v,k)
#     tmp.append(newt)
#
# tmp = sorted(tmp)
# print('Sorted', tmp)
# for v,k in tmp :
#     print(k,v)
