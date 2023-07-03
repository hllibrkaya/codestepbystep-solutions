def factorial(n):
    fact=1
    if n==0 or n==1:
        print(n, "factorial = 1")
        return
    if n<0:
        print("ERROR!")
        return
    for i in range(n,0,-1):
        fact*=i
    
    print(n, "factorial =", fact)