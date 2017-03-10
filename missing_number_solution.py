def find_missing(list1, list2):
     
    missing = set(list1) ^ set(list2)
    
    if len(list1) !=0 and  len(list2) != 0:
        if list1 == list2:
            return 0
            
        else:
            return list(missing)[0]
            
    else:
        return 0 