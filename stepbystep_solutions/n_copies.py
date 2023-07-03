def  n_copies(li1):
    newLi = []
    for i in li1:
        if i <+ 0:
            continue
        else:
            for k in range(0, i):
                newLi.append(i)
    return newLi