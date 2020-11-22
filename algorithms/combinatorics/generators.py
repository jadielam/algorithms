def product(pool: list, k: int):
    '''
    Given a pool of entries, returns a list with all possible
    products of size k from that pool.  if len(pool) = n, there
    will be n^k entries in the list to be returned.
    '''
    to_return = [[]]
    for _ in range(k):
        to_return = [a + [b] for a in to_return for b in pool]
    return to_return

def permutations_from_product(l: list, k: int):
    '''
    Given a list l of elements, returns all possible permutations of the list
    of size k. k must be less than or equal to the length of the list.
    If n is the length of the list, the number of possible permutations is
    equal to n!/(n - k)!
    '''
    indexes = list(range(len(l)))
    indexes_products = product(indexes, k)
    to_keep = [p for p in indexes_products if len(set(p)) == k]
    to_return = []
    for entry in to_keep:
        p_entry = []
        for index in entry:
            p_entry.append(l[index])
        to_return.append(p_entry)
    return to_return

        
def combinations_from_product(l: list, k: int):
    '''
    Given a list l of elements, returns all possible combinations of 
    k elements from the list. k must be less than or equal to the length of
    the list.
    If n is the length of the list, the number of possible permutations is
    equal to n!/((n-k)!n!)
    '''
    indexes = list(range(len(l)))
    indexes_products = product(indexes, k)
    to_keep = [p for p in indexes_products if len(set(p)) == k]
    combinations = {tuple(sorted(p)) for p in to_keep}
    to_return = []
    for entry in combinations:
        c_entry = []
        for index in entry:
            c_entry.append(l[index])
        to_return.append(c_entry)
    return to_return

def combinations_from_permutations(l: list, k: int):
    '''
    Given a list l of elements, returns all possible combinations of 
    k elements from the list. k must be less than or equal to the length of
    the list.
    If n is the length of the list, the number of possible permutations is
    equal to n!/((n-k)!n!)
    '''
    n = len(l)
    to_return = []
    for indices in permutations(list(range(n)), k):
        if sorted(indices) == list(indices):
            to_return.append(indices)
    return to_return

def combinations_with_replacement_from_product(l: list, k: int):
    '''
    Given a list l of elements, returns all possible combinations of r elements
    from the list. r must be less than or equal to the length of the list.
    If n is the length of the list, the number of possible combinatinos with replacement is
    equal to (n + k - 1)!/(k!(n + k - 1 - k)!)
    '''
    n = len(l)
    to_return = []
    for indices in product(list(range(n)), k):
        if sorted(indices) == list(indices):
            to_return.append(indices)
    return to_return

def permutations(iterable, r = None):
    '''
    This is close to the official Python itertools library implementation.
    '''
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    to_return = []
    to_return.append(tuple(pool[i] for i in indices[:r]))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                # Send number to the back of the line
                indices[i:] = indices[i+1:] + indices[i:i+1]
                # Restart count again
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                to_return.append(tuple(pool[i] for i in indices[:r]))
                break
        else:
            return to_return

def combinations(l: list, k: int):
    '''
    Given a list l of elements, returns all possible combinations of 
    r elements from the list. r must be less than or equal to the length of
    the list.
    If n is the length of the list, the number of possible permutations is
    equal to n!/((n-k)!n!)
    '''
    pool = tuple(l)
    n = len(pool)
    if k > n:
        return
    indices = list(range(k))
    to_return = []
    to_return.append(tuple(pool[i] for i in indices))
    while True:
        for i in reversed(range(k)):
            if indices[i] != i + n - k:
                break
        else:
            return to_return
        indices[i] += 1
        # A guarantee that we don't repeat elements
        # Do we need it?
        for j in range(i + 1, k):
            indices[j] = indices[j - 1] + 1
        to_return.append(tuple(pool[i] for i in indices))
    return to_return

def combinations_with_replacement(l: list, k: int):
    '''
    Given a list l of elements, returns all possible combinations of r elements
    from the list. r must be less than or equal to the length of the list.
    If n is the length of the list, the number of possible combinatinos with replacement is
    equal to (n + k - 1)!/(k!(n + k - 1 - k)!)
    '''
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(l)
    n = len(pool)
    if not n and k:
        return
    indices = [0] * k
    to_return = []
    to_return.append(tuple(pool[i] for i in indices))
    while True:
        for i in reversed(range(k)):
            if indices[i] != n - 1:
                break
        else:
            return to_return
        indices[i:] = [indices[i] + 1] * (k - i)
        to_return.append(tuple(pool[i] for i in indices))
