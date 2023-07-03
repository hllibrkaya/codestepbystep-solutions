print("This program converts feet and inches to centimeters.")
feet=int(input("Enter number of feet: "))
inch=int(input("Enter number of inches: "))
total_inch= 12*feet
total_inch+=inch
cm=2.54*total_inch
print(feet,"ft", inch, "in =", cm, "cm")