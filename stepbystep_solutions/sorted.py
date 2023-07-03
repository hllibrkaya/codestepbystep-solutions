def sorted(list):
    status= True
    for i in range(0,len(list)):
        a=list[i]
        for j in range(i+1,len(list)):
            if a>list[j]:
                status= False
    return status