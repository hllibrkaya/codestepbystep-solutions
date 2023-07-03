def find_median(arr):
    for i in range(0,len(arr)-1):
           for j in range(0,len(arr)-1):
                if(arr[j+1]<arr[j]):
                    x=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=x;
    if len(arr)==1:
        return arr[0]
    else:
        return arr[len(arr)//2]