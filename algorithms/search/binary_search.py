def binary_search(a: list, i: int, j: int, n: int):
    '''
    Searches for number n in array a[i:j].
    We assume that array a is sorted.
    Returns None if the element is not found.

    - Arguments:
        - a: list of entries
        - i: starting point of search (inclusive)
        - j: ending point of search (exclusive)
        - n: number to be searched
    '''
    while j > i:
        m = i + (j - i) // 2
        if a[m] == n:
            return n
        elif n > a[m]:
            i = m + 1
        else:
            j = m
    return None
    