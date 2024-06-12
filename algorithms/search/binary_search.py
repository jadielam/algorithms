def binary_search(a: list, i: int, j: int, n: int):
    '''
    Searches for number n in array a[i:j].
    We assume that array a is sorted.
    Returns -1 if the element is not found,
    otherwise returns the index of the element

    - Arguments:
        - a: list of entries
        - i: starting point of search (inclusive)
        - j: ending point of search (exclusive)
        - n: number to be searched
    '''
    lo = i
    hi = j - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == n:
            return mid
        elif a[mid] < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
    