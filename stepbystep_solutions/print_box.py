def print_box(filePath,number):
    f = open(filePath, "r")
    a = f.read().lower().replace("_", "").splitlines()
    print("#" * number)    
    for i in range (0, len(a)):
        a2 = a[i].capitalize()
        if(a2 == ""):
            print("#"+(" "*(number-2))+"#")
        elif(len(a2) > number):
            print("#"+a2[0:number-2]+"#")
        else:
            print("#"+a2[0:number-2]+(" "*(number-len(a2)-2))+"#")
    print("#" * number)    
    f.close()