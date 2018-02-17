import numpy as np

def elements_twice_min(arr):
    """
    Return all elements of array arr that are greater than or equal to 2 times
    the minimum element of arr.

    Parameters
    ----------
    arr: NumPy array (n, m)

    Returns
    -------
    NumPy Array, a vector of size between: 0 and (n * m) - 1
    """
    result = np.array([])
    for row in arr:
        result = np.append(result, row[row >= 2 * np.amin(arr)])
    return result

b = np.array([[1,2],[3,4],[5,6]])

print(elements_twice_min(b))
