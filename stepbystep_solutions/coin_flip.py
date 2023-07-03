import random
def coin_flip(k,chr):
    if k<0:
        print("ERROR!")
        return
    count=0
    if chr=="H":
        while count<k:
            side = random.randint(0, 1)
            if side==1:
                print(chr, end=" ")
                count+=1
            elif side==0:
                print("T", end=" ")


    elif chr=="T":
        while count<k:
            side = random.randint(0, 1)
            if side==1:
                print(chr, end=" ")
                count+=1
            elif side==0:
                print("H", end=" ")
    else:
        print("ERROR!")
        return

    print("\nYou got", chr, k, "times in a row!")
