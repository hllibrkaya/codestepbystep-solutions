def find_range_2d(a):
    if(a==[]):
        return 0
    series=[]
    for i in a:
        for c in i:
            series.append(c)
    v = max(series)- min(series)
    return v+1	