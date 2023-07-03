def flip_lines(text):
    x=open(text).readlines()
    for i in range(0,len(x)-1,+2):
        temp=x[i]
        x[i]=x[i+1]
        x[i+1]=temp
    for j in range(0,len(x)):
        if(j%2==0):
            x[j]=x[j].upper()
        else:
            x[j]=x[j].lower()
        print(x[j],end="")