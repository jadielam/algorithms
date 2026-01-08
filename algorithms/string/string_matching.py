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

def rabin_karp_string_matching(t: str, p: str):
    '''
    Finds all valid shifts where pattern p occurs in string s using
    the Rabin-Karp algorithm. If m = len(p) and n = len(t), this runs
    in expected time O(n + m) and worst-case time O(nm)

    NOTE: This implementation was done by an LLM and has not been manually
    reviewed for correctness yet.
    '''
    d = 256  # Number of characters in the input alphabet
    q = 101  # A prime number

    M = len(p)
    N = len(t)
    # Handle empty pattern: match at every shift (0..N)
    if M == 0:
        return list(range(N + 1))
    p_hash = 0  # hash value for pattern
    t_hash = 0  # hash value for text
    h = 1
    valid_shifts = []

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p_hash = (d * p_hash + ord(p[i])) % q
        t_hash = (d * t_hash + ord(t[i])) % q

    for i in range(N - M + 1):
        if p_hash == t_hash:
            if t[i:i + M] == p:
                valid_shifts.append(i)

        if i < N - M:
            t_hash = (d * (t_hash - ord(t[i]) * h) + ord(t[i + M])) % q

            if t_hash < 0:
                t_hash += q

    return valid_shifts