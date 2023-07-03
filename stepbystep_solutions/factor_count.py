def factor_count(num):
    counter = 0
    for i in range(1,num+1):
        if(num%i== 0):
            counter +=1
    return counter