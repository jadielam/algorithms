def naive_string_matching(t: str, p: str):
    '''
    Finds all valid shifts where pattern p occurs in string s
    '''
    valid_shifts = []
    for i in range(len(t) - len(p) + 1):
        if t[i:i + len(p)] == p:
            valid_shifts.append(i)
    return valid_shifts

def automata_string_matching(t: str, p: str):
    pass

