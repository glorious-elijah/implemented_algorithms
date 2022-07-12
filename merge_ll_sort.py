from linked_list import linked_list

def merge_sort(data, rev = False):
    '''
        Takes an unsorted data argument and returns a new sorted list. Returns list in ascending order if rev is False and vice versa
    '''

    if data.size_of() <= 1:
        return data
    elif data.head == None:
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
    left_half = linked_list()
    right_half = linked_list()
    current = data.head
    
    for i in range(size):
        if i < (size // 2):
            left_half.prepend(current.data)
            current = current.next_node
        else:
            right_half.prepend(current.data)
            current = current.next_node

    return left_half, right_half

# BUG
# only able to sort the first two elements correctingly
def sort(arg1, arg2, rev):
    '''
        Sorts arguments supplied in ascending order when the rev(reverse) argument is False and descending order when rev is True
        and returns a new sorted list
    '''
    new_list = linked_list()
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
        
    else:
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

l = linked_list()
l.prepend(66) 
l.prepend(63242341)
l.prepend(62345)
l.prepend(46)
l.prepend(62)
l.prepend(446)
l.prepend(62)
l.prepend(464)
l.prepend(4327)
l.prepend(66)
l.insert(12)
print('unsorted: ', l)
# print('divide', divide(l))
print('Sorted descending: ', merge_sort(l, True))
print('Sorted ascending: ', merge_sort(l))