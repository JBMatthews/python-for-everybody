# Input Setup
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)


# Variables
ot = h - 40
otrt = r * 1.5
reg = 40 * r


# The Sauce
if h <= 40:
    print(reg)
elif h > 40:
    print(reg + ot * otrt)
else :
    print("Not sure what happened!")
