def insertion_sort(nums: list) -> list:
    '''
    Sorts a list in place, in O(n^2) where n is the length of the list.
    The algorithm is stable.
    '''
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums