def box_of_stars(w,h):
    print("*"*w)
    for i in range(1,h-1):
        print("*"," "*(w-4),"*")
    print("*" * w)