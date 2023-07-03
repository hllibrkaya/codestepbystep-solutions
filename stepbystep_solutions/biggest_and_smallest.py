a=int(input("How many numbers? "))
max=float('-inf')
min=float('inf')
for i in range(a,0,-1):
    b=int(input("Next number? "))
    if b>max:
        max=b
    if b<min:
        min=b
print("Biggest =", max)
print("Smallest =", min)