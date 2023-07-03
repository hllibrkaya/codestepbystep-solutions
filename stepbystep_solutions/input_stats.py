def input_stats(fileName):
    file=open(fileName,"r")
    arr=file.read().splitlines()
    max=0
    sum=0
    for i in range(len(arr)):
        print("Line",(i+1), "has",(len(arr[i])),"chars")
        sum += len(arr[i])
        if(len(arr[i])>max):
            max=len(arr[i])

    print(len(arr),"lines; longest =",str(max)+", average =",(sum/len(arr)))