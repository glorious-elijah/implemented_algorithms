def  recursive_binary_search(list, target):
    '''
        sort list, find target and return index of target 
    '''
    sorted_list = sorted(list)
    first = 0
    last = len(sorted_list) - 1

    if(len(list) == 0):
        return False
    else:
        mid = (first + last) // 2
        if(target == list[mid]):
            return True
        elif(target > list[mid]):
            new_list = sorted_list[(mid + 1):]
            return  recursive_binary_search(new_list, target)
        else:
            new_list = sorted_list[:(mid - 1)]
            return  recursive_binary_search(new_list, target)
