def swap_pairs(lst):
    if len(lst) % 2 == 0:
        
        for i in range(0, len(lst), 2):
            
            lst[i], lst[i+1] = lst[i+1], lst[i]
            
    else:
        for i in range(0, len(lst)-2, 2):
            
            lst[i], lst[i+1] = lst[i+1], lst[i]
    print(lst)