def longest_sorted_sequence(list):
    max=0
    count=1
    for i in range(0,len(list)):
        if i!=len(list)-1:
            if list[i] <= list[i+1]:
                count+=1

            elif list[i]> list[i+1] :
                if count>max:
                    max=count
                    count=1
                else:
                    count=1
        else:
            if count > max:
                max = count

    return max