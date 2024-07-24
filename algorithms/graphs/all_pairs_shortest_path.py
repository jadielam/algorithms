import numpy as np

def extend_shortest_path(L_i: np.ndarray, W: np.ndarray):
    '''
    - Arguments:
        - L_i (n, n): contains shortest paths of length i
        - W (n, n): The weight matrix, which is multiplied by extend_shortes path procedure
    '''
    L_i1 = np.zeros(L_i.shape)
    for i in range(L_i1.shape[0]):
        for j in range(L_i1.shape[1]):
            L_i1 = np.min(L_i[i,:] + W[:,j])
    return L_i1

def slow_all_pairs_shortest_path(W : np.ndarray) -> np.ndarray:
    '''
    The runtime of this algorithm is n^4 where n is the number of vertices of the graph

    - Arguments: 
        - W: Weights adjacency matrix of shape (n, n) where n is the number of nodes in the graph.
            W[i, i] = 0
            W[i, j] = float('inf') if edge does not exist in the graph
    '''
    n = W.shape[0]
    L_1 = W     #L_1 contains all shortest paths of length 1
    L_previous = L_1
    for m in range(2, n):
        L_m = extend_shortest_path(L_previous, W)
        L_previous = L_m
    return L_previous

def fast_all_pairs_shortest_path(W: np.ndarray) -> np.ndarray:
    '''
    The runtime of this algorithm is n^3log(n)
    
    TODO: I have my suspicions that this does not work. But we need to prove it.
    The reason why I think it does not work is because is not being careful with 
    the boundaries, but I need to check that more carefully. Otherwise, the logic
    seems sound.
    
    - Arguments: 
        - W: Weights adjacency matrix of shape (n, n) where n is the number of nodes in the graph.
            W[i, i] = 0
            W[i, j] = float('inf') if edge does not exist in the graph
    '''
    n = W.shape[0]
    L_1 = W
    L_previous = L_1
    i = 1
    while i < n - 1:
        L_2i = extend_shortest_path(L_previous, L_previous)
        L_previous = L_2i
        i = 2 * i
    return L_previous


    