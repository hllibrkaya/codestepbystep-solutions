def binary_to_decimal(n):
    num=n
    dec=0
    base=1
    temp=num
    while temp:
        last= temp%10
        temp = temp//10
        dec+=last*base
        base= base*2
    return dec