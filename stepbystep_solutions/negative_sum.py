def negative_sum(fileName):
    file=open(fileName,"r")
    arr=file.read().split(" ")
    isNegative = False
    for i in range(1,len(arr)+1):
        sum=0
        for j in arr[0:i]:
            sum+=int(j)
        if(sum<0):
            print(sum,"after",i,"steps")
            isNegative=True
            return True
    if(not isNegative):
        print("no negative sum")
        return False