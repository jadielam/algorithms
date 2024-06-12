from typing import List

def counting_sort(A: List[int]) -> List[int]:
    """
    The idea behind counting sort is to create two arrays:
    1. In array C we store at index i the number of elements less than or equal to 
    the element of value i + min_v in A.
    2. Then we create an array B that will have the sorted elements of A, 
    and we iterate over A in reverse order to keep the sorting stable.
    """
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

def split_int_to_digits(a: int) -> List[int]:
    """
    Returns the digits of a number as a list of integers, and
    in reverse order of their appearance in the number.
    """
    if a == 0:
        return [0]
    else:
        number_digits = []
        t = a
        while t > 0:
            t, rem = divmod(t, 10)
            number_digits.append(rem)
        return number_digits

def split_to_digits(A: List[int]) -> List[List[int]]:
    """
    Given a list of integers, we split each integer into its digits.
    The result is a list of lists of integers.  The order of the digits
    in the internal list are in the reverse order
    """
    return [split_int_to_digits(a) for a in A]


def radix_sort(A: List[int]) -> List[int]:
    splitted_list = split_to_digits(A)
    max_nb_digits = max([len(a) for a in splitted_list])
    
    # TODO: Continue working here.
    for i in range(max_nb_digits):
        # Totally doable
        pass
