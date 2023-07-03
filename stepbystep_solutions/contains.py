def contains(a,b):
    if(a==b):
        return True
    else:
        for i in range(len(a)-3):
            if a[i:i+3]==b[:]:
                return True
        return False