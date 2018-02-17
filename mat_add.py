import numpy as np

def mat_addition(A, B):
    """
    Add vector/matrix arrays A and B together. If they cannot be added
    return False.

    Parameters
    ----------
    A: NumPy array size of (n,) or (n, m)
    B: NumPy array size of (p,) or (p, q)

    Returns
    -------
    NumPy Array of same size as A and B, or False if their sizes differ.
    """
    # Return False if shape doesn't match
    if np.shape(A) != np.shape(B):
        return False

    #create empty array - shape n, q
    result = np.zeros(np.shape(A))
    #If matrix do this
    if A.ndim == 2:
        #update each cell of result array by adding correct cells
        for r in range(np.shape(A)[0]):
            for c in range(np.shape(A)[1]):
                result[r,c] = A[r,c] + B[r,c]
        return result
    #If vector do this
    elif A.ndim == 1:
        for i in range(len(A)):
            result[i] = A[i] + B[i]
        return result
    #Else return False
    else:
        return False

b = np.array([1,2])
c = np.array([1,1])

print(mat_addition(b,c))
