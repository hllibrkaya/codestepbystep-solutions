def collapse_pairs(a):
    lst=[]
    for i in range(0,len(a)-1,2):
        x=a[i]+a[i+1]
        if(x%2!=0):
            a[i]=0
            a[i+1]=x
        else:
            a[i]=x
            a[i+1]=0