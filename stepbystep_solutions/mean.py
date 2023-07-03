def mean(x):
    s = 0
    for i in x:
        s+=i

    if s != 0 :
        return round(s /(len(x)), 1)
    else:
        return 0.0