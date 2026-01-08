def simplified_regular_expression(t: str, p: str):
    '''
    Given a text and a pattern, return True if text matches
    pattern, otherwise return False.

    '.' in pattern matches any character.
    '*' in pattern matches previous character 0 or more times
    '''
    
    memo = {}
    def dp(i: int, j: int):
        '''
        Returns True if p[j:] matches t[i:].
        How to analyze the runtime of this function:
        There are O(len(t) * len(p)) different (i, j) pairs. Each pair is computed only once and stored
        in memo. Each computation takes O(1) time. Therefore, the total runtime is O(len(t) * len(p))

        If we did not use memoization, the runtime would be exponential because each call to dp
        can generate up to two additional calls to dp.
        '''
        if not (i, j) in memo:
            # Notice that we need to check for the pattern end, not for the text end.
            # The text can end without the pattern ending and the text can still be a match due to the
            # star operator
            if j == len(p):
                ans = i == len(t)
            else:
                first_match = i < len(t) and p[j] in {t[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    ans = first_match and dp(i + 1, j) or dp(i, j + 2)
                else:
                    ans = first_match and dp(i + 1, j + 1)
            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)

def regular_expression(t: str, p: str):
    '''
    Given a text and a pattern, return True if text
    matches pattern, otherwise return False.

    Definition of a pattern:
    Let Z be an alphabet. The following is a regular expression:
    1. The empty string and a for every a in Z
    2. Let u and v be regular expressions:
    2.1 (u|v)
    2.2 (uv)
    2.3 (u*)
    
    The following elements are not part of the alphabet:
    ) ( | and *
    '''
    pass