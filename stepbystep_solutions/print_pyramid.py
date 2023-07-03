def print_pyramid():
    for i in range(1,7):
        for j in range(0,7-i):
            print(" ", end="")
        for j in range(1,2*i):
            print("*",end="")
        print()