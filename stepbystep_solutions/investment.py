def money():
    money = float(input("Initial amount? "))
    return money
def rate():
    rate = float(input("Interest rate%? "))
    return rate
def month():
    month = int(input("Num. of months? "))
    return month
for i in range(1,3):
    print("Investor",i)
    c=money()
    d=rate()
    e=month()
    amount =(c*((1+d)**e))
    print("Amount:","$",end=" ")
    print("%.2f" % round(amount, 2))
    profit =amount-c
    print("Profit:","$",end=" ")
    print("%.2f" % round(amount-c, 2),end=" ")
    n=round(profit/c*100)
    print("=",n, "%")
    if(n<=10):
        print("Weak")
    elif(n<=50):
        print("Medium")
    else:
         print("Strong")
    print()
print("Have a nice day!")
