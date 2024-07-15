from typing import List, Tuple

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
    in reverse order of their appearance in the number, meaning that
    if number is 123, the result will be [3, 2, 1]
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

def counting_sort_for_radix_sort(
        A: List[Tuple[int, List[int]]], pos: int
    ) -> List[Tuple[int, List[int]]]:
    """
    The counting_sort for radix sort follows the same
    strategy as the normal counting sort, just that it
    knows that number of unique entries is 10 (digits from 0 to 9).
    And also, the input includes the original numbers in the list.

    Arguments:
    - A: The list of numbers to sort. The first entry in the tuple
    is the number. The second entry is the number split into digits,
    in reverse order, that is, if number is 123, the second entry is
    [3, 2, 1]
    - pos: The position of the digit to sort by. The least significant
    digit is at position 0, the second least significant digit is at
    position 1, and so on.  If a number does not have a digit at the
    position we are sorting, we consider it to be 0.
    """
    C = [0] * 10
    B = [None] * len(A)

    for num, digits in A:
        digit_val = 0 if pos >= len(digits) else digits[pos]
        C[digit_val] += 1
    
    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(len(A) - 1, -1, -1):
        num, digits = A[i]
        digit_val = 0 if pos >= len(digits) else digits[pos]
        B[C[digit_val] - 1] = (num, digits)
        C[digit_val] -= 1

    return B
        

def radix_sort(A: List[int]) -> List[int]:
    if not A:
        return A
    splitted_list = split_to_digits(A)
    max_nb_digits = max([len(a) for a in splitted_list])
    input_to_sort = list(zip(A, splitted_list))

    for i in range(max_nb_digits):
        input_to_sort = counting_sort_for_radix_sort(input_to_sort, i)
    return [num for num, _ in input_to_sort]    
    
