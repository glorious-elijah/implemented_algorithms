'''
Implementation of a merge sort on a linked list
'''
from linked_list import LinkedList

def merge_sort(data, rev = False):
    '''
        Takes an unsorted data argument and returns a new sorted list.
        Returns list in ascending order if rev is False and vice versa
    '''

    if data.size_of() <= 1:
        return data
    elif data.head is None:
        return data
    #divide function returns a splitted list
    left_half, right_half = divide(data)
    #recursively call merge sort on both halves till only a single element or empty array remains
    left = merge_sort(left_half, rev)
    right = merge_sort(right_half, rev)

    return sort(left, right, rev)

def divide(data): #functional
    '''
        Takes a list argument and divides it into two different list
    '''
    size = data.size_of()
    left_half = LinkedList()
    right_half = LinkedList()
    current = data.head
    for i in range(size):
        if i < (size // 2):
            left_half.prepend(current.data)
            current = current.next_node
        else:
            right_half.prepend(current.data)
            current = current.next_node

    return left_half, right_half

def sort(arg1, arg2, rev):
    '''
        Sorts arguments supplied in ascending order when the rev(reverse)
        argument is False and descending order when rev is True
        and returns a new sorted list
    '''
    new_list = LinkedList()
    l_current = arg1.head
    r_current = arg2.head

    if rev:
        while l_current and r_current:
            if l_current.data > r_current.data:
                new_list.append(l_current.data)
                l_current = l_current.next_node

            else:
                new_list.append(r_current.data)
                r_current = r_current.next_node

        while l_current:
            new_list.append(l_current.data)
            l_current = l_current.next_node

        while r_current:
            new_list.append(r_current.data)
            r_current = r_current.next_node
        return new_list

    while l_current and r_current:
        if l_current.data < r_current.data:
            new_list.append(l_current.data)
            l_current = l_current.next_node

        else:
            new_list.append(r_current.data)
            r_current = r_current.next_node


    while l_current:
        new_list.append(l_current.data)
        l_current = l_current.next_node


    while r_current:
        new_list.append(r_current.data)
        r_current = r_current.next_node
    return new_list
