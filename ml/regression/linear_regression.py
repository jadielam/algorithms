import numpy as np

def get_gradient(w: np.ndarray, x: np.ndarray, y: np.ndarray):
    y_estimate = x.dot(w).flatten()
    error = (y.flatten() - y_estimate)
    gradient = -(1.0 / len(x)) * error.dot(x)
    return gradient, np.pow(error, 2)


def gradient_descent(w: np.ndarray, 
            train_x: np.ndarray, train_y: np.ndarray,
            alpha: float = 0.5, 
            tolerance: float = 1e-5):
    '''
    - Arguments:
        - w: shape (2,)
        -
    '''
    w = np.random.randn(2)
    alpha = 0.5
    tolerance = 1e-5

    # Perform Gradient Descent
    iterations = 1
    while True:
        gradient, error = get_gradient(w, train_x, train_y)
        new_w = w - alpha * gradient
        
        # Stopping Condition
        if np.sum(abs(new_w - w)) < tolerance:
            print("Converged.")
            break
        
        # Print error every 50 iterations
        if iterations % 100 == 0:
            print("Iteration: %d - Error: %.4f" % (iterations, error))
        
        iterations += 1
        w = new_w
    
    return w