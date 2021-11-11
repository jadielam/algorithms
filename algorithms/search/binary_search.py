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
    while j > i:
        m = i + (j - i) // 2
        if a[m] == n:
            return m
        elif n > a[m]:
            i = m + 1
        else:
            j = m
    
    m = i + (j - i) // 2
    if a[m] == n:
        return m
    else:
        return -1
    