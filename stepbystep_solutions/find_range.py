def find_range(a):
    if(min(a)==max(a)):
        return 1
    elif(len(a)==1):
        return 1
    else:
        return max(a)-min(a)+1