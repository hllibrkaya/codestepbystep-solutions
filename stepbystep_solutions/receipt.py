def main():
    a=38
    b=40
    c=30
    sub=a+b+c
    tax=sub*0.08
    tip= sub* 0.15
    print("Subtotal:", end=" ")
    print(sub)
    print("Tax:", end=" ")
    print(tax)
    print("Tip:", end=" ")
    print(tip)
    print("Total:", end=" ")
    print(sub+tax+tip)

main()