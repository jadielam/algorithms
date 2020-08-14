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