from .quicksort import randomized_partition


def select_k(a, p, r, i):
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
    