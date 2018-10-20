# Assignment 6.5 - Data Structures
#
# Instruction: Write code using find() and string slicing to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

xpos = text.find("0")

ypos = text.find("5")

solve = text[xpos : ypos + 1]

print(float(solve))
