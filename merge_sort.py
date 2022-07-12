import linked_list

def merge_sort(data, rev = False):
    '''
        Takes an unsorted data argument and returns a new sorted list. Returns list in ascending order if rev is False and vice versa
    '''

    if len(data) <= 1:
        return data

    #divide function returns a splitted list
    left_half, right_half = divide(data)
    #recursively call merge sort on both halves till only a single element or empty array remains
    left = merge_sort(left_half, rev)
    right = merge_sort(right_half, rev)

    return merge(left, right, rev)

def divide(data):
    '''
        Takes a list argument and divides it into two different list
    '''
    #find the midpoint of the list supplied 
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    return left_half, right_half

def merge(arg1, arg2, rev):
    '''
        Sorts arguments supplied in ascending order when the rev(reverse) argument is False and descending order when rev is True
        and returns a new sorted list
    '''
    new_list = []
    i = 0
    j = 0

    if rev:
        while i < len(arg1) and j < len(arg2):
            if arg1[i] > arg2[j]:
                new_list.append(arg1[i])
                i += 1
            else:
                new_list.append(arg2[j])
                j += 1
        while i < len(arg1):
            new_list.append(arg1[i])
            i += 1
        while j < len(arg2):
            new_list.append(arg2[j])
            j += 1

        return new_list
        
    else:
        while i < len(arg1) and j < len(arg2):
            if arg1[i] < arg2[j]:
                new_list.append(arg1[i])
                i += 1
            else:
                new_list.append(arg2[j])
                j += 1
        while i < len(arg1):
            new_list.append(arg1[i])
            i += 1
        while j < len(arg2):
            new_list.append(arg2[j])
            j += 1
        return new_list
