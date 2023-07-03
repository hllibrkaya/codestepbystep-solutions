def has_mirror_twice(a,b):
    if(len(b)>len(a)):
        return False
    d=[]
    for i in range(len(b)-1):
        d.append(b[len(b)-1-i])    
    c=0
    c2=0
    for i in range(len(a)):
        c=0
        for j in range(len(d)):
            if(i+j<len(a)):       
                if(d[j]==a[i+j]):
                    c+=1
        if(c==len(d)):
            c2+=1    
    if(c2>=2):
        return True

    return False