def computepay(x,y):

    if x > 40 :
        reg = x * y
        otp = (x - 40.0) * (y * 0.5)
        xp = reg + otp
        return xp

    elif x < 40 :
        reglr = x * y
        return reglr

    else:
        return print("Error. Try Again.")

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h, r)

print(p)
