def days_in_month(n):

    if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12 :
        return 31
    elif n==2:
        return 28
    elif n==4 or n==6 or n==9 or n==11:
        return 30