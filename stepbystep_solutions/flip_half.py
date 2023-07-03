def flip_half(List):
    temp=List[1::2]
    temp.reverse()
    for i in range(1,len(List),2):
        List[i]=temp[int(i/2)]