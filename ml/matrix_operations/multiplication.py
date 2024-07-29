import numpy as np

def multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    if a.shape[1] != b.shape[0]:
        raise ValueError('a.shape[1] != b.shape[0]')
    
    common_type = np.find_common_type([a.dtype, b.dtype], [])
    to_return = np.empty((a.shape[0], b.shape[1]), dtype = common_type)
    
    for r in range(a.shape[0]):
        for c in range(b.shape[1]):
            # Alternative one
            val = 0
            for i in range(a.shape[1]):
                val += a[r, i] * b[i, c]
            to_return[r, c] = val
            
            # Alternative two
            # to_return[r, c] = sum(a[r, :] * b[:, c])

            # Alternative three
            # to_return[r, c] = np.dot(a[r, :], b[:, c])
    return to_return