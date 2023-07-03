def get_percent_even(a):
    count=0
    per_num=0.0
    for x in a :
        if x%2==0:
            count+=1
    if count==0:
        return 0.0
    else:
        per_num=1/len(a)*count*100
        return per_num