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

def bisect_left(a: list, x, lo=0, hi=None, *, key=lambda i, x: x):
    '''
    Finds the leftmost index where the element should be inserted in the sorted array.
    Returns the index of the element if it is found, otherwise returns the 
    index where the element should be inserted.

    - Arguments:
        - a: list of entries
        - x: value that I am searching for
        - lo: starting point of search (inclusive)
        - hi: ending point of search (exclusive)
        - key: function that takes the index and the element and returns the key to compare
            Notice that we only apply the key function to the element in the array, 
            but never to the value x we are searching for.
    '''
    if lo < 0:
        raise ValueError("lo must be non-negative")
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if key(mid, a[mid]) < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def bisect_right(a: list, x, lo=0, hi=None, *, key=lambda i, x: x):
    """
    Finds the rightmost index where the element should be inserted in the sorted array.

    - Arguments:
        - a: list of entries
        - x: value that I am searching for
        - lo: starting point of search (inclusive)
        - hi: ending point of search (exclusive)
        - key: function that takes the index and the element and returns the key to compare
            Notice that we only apply the key function to the element in the array, 
            but never to the value x we are searching for.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < key(mid, a[mid]):
            hi = mid
        else:
            lo = mid + 1
    
    return lo
