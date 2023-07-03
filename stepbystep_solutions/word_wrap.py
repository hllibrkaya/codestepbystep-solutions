def word_wrap(fileName):
    file=open(fileName,"r")
    arr=file.read().splitlines()
    for i in arr:
        if(i==""):
            print("")
        for j in range(0,len(i),60):
            print(i[j:j+60])