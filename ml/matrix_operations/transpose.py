import numpy as np

def transpose(a: np.ndarray) -> np.ndarray:
    to_return = np.empty((a.shape[1], a.shape[0]), dtype = a.dtype)
    for r in range(a.shape[0]):
        for c in range(a.shape[1]):
            to_return[c, r] = a[r, c]
    return to_return

def transpose_(a: np.ndarray):
    assert a.shape[0] == a.shape[1]
    for i in range(a.shape[0]):
        for j in range(i, a.shape[0]):
            a[i, j], a[j, i] = a[j, i], a[i, j]

