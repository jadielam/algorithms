import numpy as np
from scipy.spatial import distance

def kmeans(X, k = 3, max_iterations = 100):
    '''
    X: multidimensional data
    k: number of clusters
    max_iterations: number of repetitions before clusters are established
    
    Steps:
    1. Convert data to numpy aray
    2. Pick indices of k random point without replacement
    3. Find class (P) of each data point using euclidean distance
    4. Stop when max_iteration are reached of P matrix doesn't change
    
    Return:
    np.array: containg class of each data point
    '''
    idx = np.random.choice(len(X), k, replace = False)
    centroids = X[idx, :]
    P = np.argmin(distance.cdist(X, centroids, 'euclidean'), axis = 1)
    # P has shape (nb_entries, k)
    for _ in range(max_iterations):
        centroids = np.vstack([X[P == i, :].mean(axis = 0) for i in range(k)])
        tmp = np.argmin(distance.cdist(X, centroids, 'euclidean'), axis = 1)
        if np.array_equal(P, tmp):
            break
        P = tmp
    return P