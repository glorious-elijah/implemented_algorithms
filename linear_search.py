'''
Implementation of a linear search
'''
def linear_search(data, target):
    '''
    Returns index of target in list.
    '''
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1
