# 9.4 Assignment - testing
#
# Input File:
# mbox-short.txt
#
# Dictionary
dcnt = dict()
# Usr Prmpt
entr = input("Enter file:")
if len(entr) < 1 :
    entr = "mbox-short.txt"
handle = open(entr)
# For Loop - For every line in fh, the following is true
for line in handle:
    wds = line.split()
    # If Statement - Qualitfing the line
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    email = wds[1]
    # Dictionary Logic
    dcnt[email] = dcnt.get(email,0) + 1

    tpwrd = None
    tpcnt = None
    for word,count in dcnt.items():
        if tpcnt is None or count > tpcnt :
            tpwrd = word
            tpcnt = count

print(tpwrd,tpcnt)



# # Written code
# Open and read 'mbox-shot.txt'
#
# Look for "'From'-lines"
#
# Take second "word" from "From-Lines"
#
# Use dictionary to map sender's email with a count of Occurence
#
# Use "Maxium" Loop to loop thru dictionary to find most prolific committer
