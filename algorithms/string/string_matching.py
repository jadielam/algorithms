from typing import List

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

def compute_transition_function(p: str, alphabet = List[str]):
    '''
    Computes a transition function O(m^3*len(alphabet))
    It is possible to compute a transition function in O(m*len(alphabet))
    '''
    # TODO: Something wrong here.
    m = len(p)
    d = {}
    for q in range(0, m + 2):
        print(q)
        for a in alphabet:
            k = min(m + 1, q + 2)
            while not (p[:q] + a).endswith(p[:k]):
                k = k - 1
            d[q, a] = k
    return d
            
def automata_string_matching(t: str, p: str):
    '''
    If m = len(p) and n = len(t), 
    it runs in time O(m^3*len(alphabet) + n)
    '''
    alphabet = set(t) | set(p)
    d = compute_transition_function(p, alphabet)
    n = len(t)
    m = len(p)
    q = 0
    valid_shifts = []
    for idx, ch in enumerate(t):
        q = d[q, ch]
        if q == m:
            valid_shifts.append(idx - m)
    return valid_shifts




