def naive_string_matching(t: str, p: str):
    '''
    Finds all valid shifts where pattern p occurs in string s.
    If m = len(p) and n = len(t), this runs in time O(nm)
    '''
    valid_shifts = []
    for i in range(len(t) - len(p) + 1):
        if t[i:i + len(p)] == p:
            valid_shifts.append(i)
    return valid_shifts
