'''
    This is an implementation of the quicksort algorithm
'''
def quick_sort(data, rev = False):
    '''
    Sorts a list in ascending order by default, Passing a second
    argument a boolean value of true will sort in descending.
    '''
    if len(data) <= 1:
        return data
    less = []
    great = []
    pivot = data[0]

    for value in data[1:]:
        if value > pivot:
            great.append(value)
        else:
            less.append(value)
    if rev:
        return quick_sort(great, rev) + [pivot] + quick_sort(less, rev)
    else:
        return quick_sort(less, rev) + [pivot] + quick_sort(great, rev)
