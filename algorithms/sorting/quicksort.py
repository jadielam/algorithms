import random

def randomized_partition(a: list, p, r) -> int:
    '''
    Given list `a` and indexes `p` and `r` (both inclusive), shuffles elements in a. it returns index
    `q` such that all elements a[:q] are less than or equal to a[q] and all elements a[q+1:] are greater
    than `q`.
    
    - Arguments:
        - a: array of comparables
        - p: start index (inclusive)
        - r: end index (inclusive)
    - Returns:
        - q: partition index
    '''
    #1. Swap last element of array with partition
    q = random.randint(p, r)
    a[r], a[q] = a[q], a[r]
    
    #2. Do the partition algorithm
    i = p # next location to insert a value less than or equal to a[r]
    for j in range(p, r):
        if a[j] <= a[r]:
            a[i], a[j] = a[j], a[i]
            i += 1
    
    a[i], a[r] = a[r], a[i]
    return i
    
def quick_sort(a: list, i: int, j: int):
    '''
    Given list `a`, it sorts it in place. Fast implementations of it, and this one
    in particular are not stable. The random picking of q makes it unstable.
    It runs in average case nlog(n), but it can have a worst
    case performance of n^2. 
    
    To call function in list:
    `quick_sort(a, 0, len(a) - 1)`
    
    It does not return the list. It sorts it in place
    
    - Arguments:
      - a: list of comparables
      - i: first index of list to start sorting
      - j: last index of list to sort
    '''
    if i < j:
        q = randomized_partition(a, i, j)
        quick_sort(a, i, q - 1)
        quick_sort(a, q + 1, j)