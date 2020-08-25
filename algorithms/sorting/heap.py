def parent(cidx: int):
    '''
    Returns the index of the parent to cidx
    '''
    return (cidx - 1) // 2
    
def left(cidx: int):
    '''
    Returns index of left child
    '''
    return 2 * cidx + 1

def right(cidx: int):
    '''
    Returns index of right child
    '''
    return 2 * cidx + 2

def first_leaf(length: int):
    return length // 2

def max_heapify(A: list, i: int, heap_length: int):
    '''
    When ran, it assumes that the `trees` rooted at
    A[left(i)] and A[right(i)] are keep the heap 
    property, and that the value at A[i] needs to be floated down.
    '''    
    ci = i
    while True:
        li = left(ci)
        ri = right(ci)
        if li < heap_length and A[li] > A[ci]:
            largest = li
        else:
            largest = ci
        if ri < heap_length and A[ri] > A[largest]:
            largest = ri
        if largest != ci:
            temp = A[ci]
            A[ci] = A[largest]
            A[largest] = temp
            ci = largest
        else:
            break

def extract_max(A: list):
    '''
    - Arguments:
        - A: list that is a queue
    
    - Returns:
        - max_elem
    
    - Raises:
        - IndexError if heap size is less than 1
    '''
    max_elem = A[0]
    A[0] = A[len(A) - 1]
    del A[len(A) - 1]
    max_heapify(A, 0, len(A))
    return max_elem

def heap_increase_key(A: list, i: int, key):
    if key < A[i]:
        raise ValueError('key most be larger than previous key')
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        parent_i = parent(i)
        temp = A[i]
        A[i] = A[parent_i]
        A[parent_i] = temp
        i = parent_i

def heap_insert(A: list, key):
    A.append(float('-inf'))
    heap_increase_key(A, len(A) - 1, key)

def is_max_heap(A: list, heap_length: int) -> bool:
    '''
    Checks if array A keeps the heap property
    '''
    for i, a in enumerate(A):
        li = left(i)
        ri = right(i)
        if li < heap_length and A[li] > A[i]:
            return False
        if ri < heap_length and A[ri] > A[i]:
            return False
    
    return True

def build_max_heap(A: list) -> None:
    '''
    Given an array, it converts it into a max heap
    '''
    last_non_leaf = first_leaf(len(A)) - 1
    for i in range(last_non_leaf, -1, -1):
        max_heapify(A, i, len(A))

def heapsort(to_sort: list):
    '''
    Sorts in place
    '''
    build_max_heap(A)
    heap_length = len(A)
    for i in range(len(A)):
        temp = A[heap_length - 1]
        A[heap_length - 1] = A[0]
        A[0] = temp
        heap_length -= 1
        max_heapify(A, 0, heap_length)