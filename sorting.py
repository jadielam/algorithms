import random

def insertion_sort(nums: list) -> list:
    '''
    Sorts a list in place, in O(n^2) where n is the length of the list.
    The algorithm is stable.
    '''
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums

def merge(a: list, b: list) -> list:
    '''
    Given two sorted lists: a and b, it returns a third sorted list
    made of the merge of a and b.  Merging happens in O(len(a) + len(b))
    '''
    to_return = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            to_return.append(a[i])
            i += 1
        else:
            to_return.append(b[j])
            j += 1
    
    while i < len(a):
        to_return.append(a[i])
        i += 1
    while j < len(b):
        to_return.append(b[j])
        j += 1
        
    return to_return
    
def merge_sort(nums: list, i: int, j: int) -> list:
    '''
    Sorts sublist nums[i:j] and returns it sorted. It does not sort
    in place.  It is stable.  
    
    To call it from the outside, you should do:
    merge_sort(nums, 0, len(nums))
    '''
    if j <= i + 2:
        return insertion_sort(nums[i:j])
    else:
        range_ = j - i
        boundary = range_ // 2
        a = merge_sort(nums, i, i + boundary)
        b = merge_sort(nums, i + boundary, j)
        return merge(a, b)
        
def partition(a: list, p, r) -> int:
    '''
    Given list `a` and indexes `p` and `r` (both inclusive), shuffles elements in ait returns index
    `q` such that all elements a[:q] are less than or equal to q and all elements a[q+1:] are greater
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
    temp = a[r]
    a[r] = a[q]
    a[q] = temp
    
    #2. Do the partition algorithm
    i = p - 1
    j = p
    while j < r:
        if a[j] <= a[r]:
            i += 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        j += 1
    
    temp = a[i + 1]
    a[i + 1] = a[r]
    a[r] = temp
    return i + 1
    
def quick_sort(a: list, i: int, j: int):
    '''
    Given list `a`, it sorts it in place in a stable manner.
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
        q = partition(a, i, j)
        quick_sort(a, i, q - 1)
        quick_sort(a, q + 1, j)
