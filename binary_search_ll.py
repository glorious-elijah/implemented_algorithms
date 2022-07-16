'''
Searches through a linked list to find a provided key
'''
def binary_search(data,key):
    '''
    Search through the list provided and returns true if key is found
    '''
    if data.size_of() <= 1 and key != data.head.data:
        return False
    if data.head is None:
        return False

    mid = data.size_of() // 2
    current = data.at_index(mid)

    if key == current.data:
        return True
    if key < current.data:
        new_list = data.slice(0,mid)
        return binary_search(new_list, key)
    if key > current.data:
        mid += 1
        new_list = data.slice(mid)
        return binary_search(new_list, key)
