# This file exsist to test coding theory for assignment completion
## ---8.4-Assignment---
#
# User Input - Open the file romeo.txt and read it line by line.
#
fh = open("romeo.txt")
lst = list()
for line in fh:
    line = line.split()
    for wrds in line:
        if wrds not in lst:
            lst.append(wrds)
lst.sort()
print(lst)



#.sort()
# print(len(line))
# print(len(wrds))
# print(len(lst))


#-INPUT FILES
# romeo.txt
# romeo-test.txt
