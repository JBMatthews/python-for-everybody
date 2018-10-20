#
# This are all from examples giving during the video lecture
#

# Print a file out using a for loop
xfile = open('file.txt')
for line in xfile:
    print(line)

# Counting lines in a file
fhand = open('file.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# Searching through a xfile
fhand-2 = open('file.txt')
for lines in fhand-2:
    if lines.startswith('From:') :
        print(lines)
