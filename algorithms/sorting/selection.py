from quicksort import randomized_partition

def select_k(a, p, r, i):
    '''
    Returns the ith smallest element in array a[p...r]
    It finds the element in average linear time.
    Indexes `p` and `r` are inclusive.
    '''
    if p == r:
        return a[p]
    q = randomized_partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif i < k:
        return select_k(a, p, q - 1, i)
    else:
        return select_k(a, q + 1, r, i - k)
