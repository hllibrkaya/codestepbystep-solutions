def is_rotation(str1,str2):
    size1=len(str1)
    size2=len(str2)
    if size1!=size2:
        return False
    text=str1+str1
    if (text.count(str2)> 0):
        return True
    else:
        return False