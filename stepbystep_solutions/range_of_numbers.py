def range_of_numbers(a, b):
    if a<b:
        for i in range(a,b+1):
            print(a, end=" ")
            a+=1

    elif a>b:
        for i in range(a,b-1,-1) :
            print(a, end= " ")
            a-=1

    elif a==b:
        print(a)