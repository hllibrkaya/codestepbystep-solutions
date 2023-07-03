import random
x= int(input("Desired sum: "))
a = 0
b = 0 
while(a+b) != x:
    b = (random.randint(1,6))
    a = (random.randint(1,6))
    print(f"{a} and {b} = {a+b}")