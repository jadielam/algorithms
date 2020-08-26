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
        Returns True if p[j:] matches t[i:]
        '''
        if not (i, j) in memo:
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