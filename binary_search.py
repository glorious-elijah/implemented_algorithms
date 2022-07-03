def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while(first <= last):
        mid = (first + last) // 2
        if target == list[mid]:
            return mid
        elif target > list[mid]:
            first = mid + 1
        else:
            last = mid -1
    return -1

def test_search():
    assert binary_search([x for x in range(1, 11)], 5) == 4