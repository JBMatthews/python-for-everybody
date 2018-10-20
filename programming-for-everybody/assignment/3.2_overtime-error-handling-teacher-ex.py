# Input Setup
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error - Numeric Input Only Try again.")

# The Sauce
if h > 40 :
    reg = r * h
    otp = (h - 40.0) * (r * 0.5)
    xp = reg + otp
else h > 40:
    xp = h * r

print("Pay",xp)
