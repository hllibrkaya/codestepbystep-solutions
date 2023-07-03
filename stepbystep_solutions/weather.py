fileName=input("Input file? ")
file=open(fileName,"r")
arr=file.read().split()
new= []

for i in arr:
    if(i.replace(".","").isdecimal() or i.startswith("-")):
        new.append(i)

for i in range(len(new)-1):
    print(new[i],"to",new[i+1]+", change =",round((float(new[i+1])-float(new[i])),2))
