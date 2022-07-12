def binary_search(list, target):
    '''
        sort list, find target and return index of target 
    '''
    sorted_list = sorted(list)
    first = 0
    last = len(sorted_list) - 1

    while(first <= last):
        mid = (first + last) // 2
        if target == sorted_list[mid]:
            return mid
        elif target > sorted_list[mid]:
            first = mid + 1
        else:
            last = mid -1
    return -1