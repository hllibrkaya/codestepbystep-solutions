import random
def random_walk():
    position=0
    max=0
    print("position =", position)
    while position!=3 and position!=-3 :
        inc_dec=random.randrange(1,3)
        if inc_dec==1:
            position=position-1
            print("position =", position)
        else:
            position=position+1
            print("position =", position)
        if position>max:
            max=position
    print("max position =", max)