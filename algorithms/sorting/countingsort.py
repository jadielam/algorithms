from typing import List

def counting_sort(A: List[int]) -> List[int]:
    if not A:
        return []
    
    min_v = min(A)
    max_v = max(A)
    k = max_v - min_v + 1

    C = [0] * k
    B = [None] * len(A)

    for j in range(len(A)):
        C[A[j] - min_v] += 1
        # C[i] now contains the number of equal to i in A
    
    for i in range(1, len(C)):
        C[i] += C[i - 1] 
        # C[i] now contains number of elements less than or
        # equal to i
    
    for j in range(len(A) - 1, -1, -1):
        # The reason why we go on inverse order here is to 
        # have an stable sorting algorithm
        B[C[A[j] - min_v] - 1] = A[j]
        C[A[j] - min_v] -= 1

    return B

