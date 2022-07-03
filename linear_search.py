def linear_search(list, target):
    '''
    Returns index of target in list.
    '''
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def test_search():
    assert linear_search([x for x in range(1,10000)], 100) == 99

