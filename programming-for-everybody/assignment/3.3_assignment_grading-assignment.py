score = input("Enter Score: ")

try:
    scoref = float(score)
except:
    print("Error - Numberic Entries Only")
    quit()

if scoref >= 0.9 :
 	print("Grade: A")

else:
   	print("Didn't work.")

#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
