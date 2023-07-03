def print_numbers2():
    count=1
    for i in range(4, -1, -1):
        print("." * i, end="")
        print(str(count)*count)
        count+=1