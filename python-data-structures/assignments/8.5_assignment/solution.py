# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#
# Hint: make sure not to include the lines that start with 'From:'.
#
# Input File:
# mbox-short.txt
fh = open("mbox-short.txt")
# The Count
count = 0
# For Loop - For every line in fh, the following is true
for line in fh:
    line = line.rstrip()
    wds = line.split()
    # If Statement - Qualitfing the line
    if len(wds) < 3 or wds[0] != 'From' :    continue
    count = count + 1
    print(wds[1])
print("There were", count, "lines in the file with From as the first word")
