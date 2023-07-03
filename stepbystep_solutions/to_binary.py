def to_binary(n):
    rnum=""
    if n==0:
        rnum+=str(0)
    while n>0:
        rem=n%2
        n=n//2
        rnum+=str(rem)
    num=rnum[::-1]
    return num