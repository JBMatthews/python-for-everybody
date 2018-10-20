largest = None
smallest = None

while True:
# Prompt
    numin = input("Enter a number: ")

# Break
    if numin == "done":
        break

# Try & Except
    try:
        intnum = int(numin)
    except:
        print("Invalid input")


# Comparative Logic
    if largest is None:
        largest = intnum
    elif smallest is None:
        smallest = intnum
    elif intnum > largest:
        largest = intnum
    elif intnum < smallest:
        smallest = intnum
    else:
        continue



print("Maximum is ",largest)
print("Minimum is ",smallest)
