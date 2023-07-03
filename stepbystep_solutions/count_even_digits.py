def count_even_digits(num,leng):
    count=0
    str_num=str(num)
    even_count=0
    while count<leng:
        if str_num[count]=="0" or str_num[count]=="2" or str_num[count]=="4" or str_num[count]=="6" or str_num[count]=="8" :
            even_count+=1
        count+=1
    return even_count
