'''
Linked list variation of a linear search
'''

def linear_search(data, key):
    '''
    Find a key in a list and return True if present
    '''

    current = data.head

    for i in range(data.size_of()):
        if key == current.data:
            return True
        current = current.next_node

    return False
