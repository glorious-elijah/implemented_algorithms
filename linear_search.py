def linear_search(list, target):
    '''
    Returns index of target in list.
    '''
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
