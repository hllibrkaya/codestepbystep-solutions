def triangle(n):
    space=n-1
    for i in range(1,n+1):
        print(" "*space, end="")
        print("*"*i)
        space-=1