import numpy as np

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    '''
    Given two strings, returns the length of the longest common subsequence.
    - Example:
        - Input: "abcde" and "ace"
        - Longest common subsequence is "ace"
    '''
    if len(text1) == 0 or len(text2) == 0:
        return 0
        
    lcs = np.zeros((len(text1) + 1, len(text2) + 1), dtype = np.int32)
    for m in range(lcs.shape[0] - 1):
        for n in range(lcs.shape[1] - 1):
            if text1[m] == text2[n]:
                lcs[m + 1, n + 1] = lcs[m, n] + 1
            else:
                lcs[m + 1, n + 1] = max(lcs[m, n + 1], lcs[m + 1, n])
        
    return lcs[lcs.shape[0] - 1, lcs.shape[1] - 1]