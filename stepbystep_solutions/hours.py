def hours():
    fileName=input("Input file? ")
    file=open(fileName,"r")
    arr=file.read().splitlines()

    for i in arr:
        temp=i.split(" ")
        sum=0
        for j in temp[2:]:
            sum +=float(j)
        average=round( (sum/(len(temp)-2)),1)
        print(temp[1],"(ID#"+str(temp[0])+")","worked",str(round(sum,1)),"hours ("+str(average)+"/day)")








