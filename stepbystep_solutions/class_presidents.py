def class_presidents (fileName):
    file=open(fileName,"r")
    arr=file.read().split(" ")

    sName=""
    jName=""
    sVote=0
    jVote=0

    for i in range(len(arr)-2):
        if(arr[i+1] == "s" and int(arr[i+2]) > sVote):
            sName=arr[i]
            sVote=int(arr[i+2])
        elif(arr[i+1] == "j" and int(arr[i+2]) > jVote):
            jName=arr[i]
            jVote=int(arr[i+2])
    print("Sophomore Class President:",sName,"("+str(sVote),"votes)")
    print("Junior Class President:",jName,"("+str(jVote),"votes)")