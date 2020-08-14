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