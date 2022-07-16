'''
    Quicksort implementation for a linked list
'''
from linked_list import LinkedList

def quick_sort(data, rev = False):
    """
    Purpose: Sorts a list passed as argument, default sort is ascending
    passing a second argument of True will sort in descending
    """
    if data.size_of() <= 1:
        return data
    if data.head is None:
        return data

    current = data.head.next_node
    pivot = data.head
    less_than = LinkedList()
    greater_than = LinkedList()

    while current:
        if current.data <= pivot.data:
            less_than.append(current.data)
            current = current.next_node
        else:
            greater_than.append(current.data)
            current = current.next_node
    if rev:
        return f'{quick_sort(greater_than, rev)} {pivot} {quick_sort(less_than, rev)}'

    return f'{quick_sort(less_than, rev)} {pivot} {quick_sort(greater_than, rev)}'
# end def
