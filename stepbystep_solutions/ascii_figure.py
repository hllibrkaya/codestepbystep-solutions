def ascii_figure ():
    j=16
    k=0
    for i in range(1,6):
            print("/"*j,end="")
            print("*"*k,end="")
            print("\\"*j,end="")
            print()
            j-=4
            k+=8