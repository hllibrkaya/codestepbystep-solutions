def intersect(dict1,dict2):
    myDict = {}
    for k,v in dict1.items():
        for x,y in dict2.items():
            if k ==x:
                if v==y:
                    upd={k:v}
                    myDict.update(upd)
    return myDict