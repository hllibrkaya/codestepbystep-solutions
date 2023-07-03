def is_prime_number (num):
    prime=True
    if num==2:
        prime=True
    if num<=1:
        prime=False
    for i in range(2,num):
        if num%i==0:
            prime=False
    return prime