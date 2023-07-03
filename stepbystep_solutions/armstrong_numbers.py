def armstrong_numbers(n):
    if n<=0:
        return 0
    low_lim = 10 ** (n - 1)
    if n==1:
        low_lim=0
    up_lim = 10 ** n
    for i in range(low_lim, up_lim):
        temp = i
        sum = 0
        for j in range(0, n):
            sum += (temp % 10) ** n
            temp = temp // 10
        if sum == i:
            print(i, end=" ")