def palabra(palabra):
    my_set = set()
    
    for l in palabra:
        my_set.add(l)
        
    my_list = list(my_set)
    my_list.sort()
    
    print(my_list)
        
palabra('palabra')