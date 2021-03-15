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


def split_to_digits(A: List[int]):
    splitted_list = []
    for a in A:
        number_digits = []
        t = a
        if t == 0:
            number_digits.append(0)
        else:
            while t > 0:
                div, rem = divmod(t, 10)
                number_digits.append(rem)
                t = div
        splitted_list.append(number_digits)
    return splitted_list

def radix_sort(A: List[int]) -> List[int]:
    splitted_list = split_to_digits(A)
    max_nb_digits = max([len(a) for a in splitted_list])
    
    # TODO: Continue working here.
    for i in range(max_nb_digits):
        pass
