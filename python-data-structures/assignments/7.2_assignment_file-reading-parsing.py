# Assignment 7.2 - Data Structures
#
# Instruction: Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#                 X-DSPAM-Confidence:  0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#
#
# Use the file name mbox-short.txt as the file name
#
# Desired Output:
# Average spam confidence: 0.750718518519
#

# Input
fname = input("Enter file name: ")
fh = open(fname)
# Logic
count = 0
total = 0.0
for line in fh:
    # Catcher
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line.find("0")
    y = line.find(' ',x)
    data = float(line[x : y])
    # Avg Calc
    total = total + data
    count = count + 1
    avg = total / count
# Final Print
print("Average spam confidence:",avg)
