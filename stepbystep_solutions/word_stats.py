def word_stats(fileName):
    file=open(fileName,"r")
    word=file.read()
    
    print("Total words    =" , len((word.split())))

    new=word.split()
    sum=0
    for i in new:
        sum += len(i)
    print("Average length =",sum/len(new))

    counter=0
    for i in set(word.lower().replace(" ","")):
        if(i not in __import__('string').punctuation):
            counter +=1
    print("Unique letters =",counter-1)