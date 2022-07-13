'''
Implementation of the binary search algorithm
'''
def binary_search(data, target):
    '''
        sort data, find target and return index of target
    '''
    sorted_list = sorted(data)
    first = 0
    last = len(sorted_list) - 1

    while first <= last:
        mid = (first + last) // 2
        if target == sorted_list[mid]:
            return mid
        if target > sorted_list[mid]:
            first = mid + 1
        else:
            last = mid -1
    return -1
