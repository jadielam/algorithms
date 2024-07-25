from .quicksort import randomized_partition


def select_k(a, p, r, i):
    """
    This algorithm runs in linear time.  The reason is this one:
    n + n/2 + n/4 + n/8 + ... 1 is approximately equal to 2n.

    In order to show the claim above, see the formula:
    sum from 0 to n - 1 of a(r^k) is equal to a[(1 - r^n)/(1 - r)]

    This is the same formula we use to compute 2^0 + ... 2^n = 2^(n+1) - 1
    But in this case, we use it in this way: a = n and r = (1/2)
    
    Arguments:
    - a: array
    - p: starting index inclusive
    - r: ending index inclusive
    - i: index to select, 1-indexed.
    """
    if i > len(a):
        raise ValueError("Index i is greater than the length of the array")
    if i <= 0:
        raise ValueError("Index i must be greater than 0")
    
    q = randomized_partition(a, p, r)
    if q == i - 1:
        return a[q]
    elif q < i - 1:
        return select_k(a, q + 1, r, i)
    else:
        return select_k(a, p, q - 1, i)
    