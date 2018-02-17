import numpy as np

def dot_product(a, b):
    '''
    Return the dot product of two numpy arrays of the same length.

    Parameters
    ----------
    a: numpy array with shape (n, )
        An array of floating point numbers.
    b: numpy array with shape (n, )
        An array of floating point numbers.

    Returns
    -------
    dot_prod: float
        The dot product of a and b.
    '''
    result = 0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result

def mat_inner_product(X, Y):
    '''
    Multiply two numpy arrays, if possible.

    Parameters
    ----------
    X: array, shape (n, m)
    Y: array, shape (p, q)

    Returns
    -------
    ret: array, shape (n, q), or False
        If the two arrays cannot be multiplied (X times Y), then return False.
        Otherwise return the product.
    '''
    # Return False if number of columns in X doesn't match number of rows in Y
    if len(X[0]) != len(Y):
        return False

    #create empty array - shape n, q
    result = np.zeros((len(X),len(Y[0])))

    #update each cell of result array by computing dot product of the correct columns
    for r in range(len(result)):
        for c in range(len(result[0])):
            result[r][c] = dot_product(X[r],Y[:,c])

    return result

def xtx_product(X):
    """
    Given a matrix X, calculate the inner product X^T X, where the ^T
    operator denotes the transpose.

    Parameters
    ----------
    X: NumPy array size of (n, m)

    Returns
    -------
    NumPy Array of size (m, m)
    """
    return mat_inner_product(np.transpose(X),X)

import itertools

def permutations_in_dict(string, words):
    '''
    Use itertools.permutations to return all the permutations of the string
    and return only the ones which are members of set words.

    Parameters
    ----------
    string : {str}
    words : {set}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'})
    ['act', 'cat']
    '''
    return list(set([''.join(x) for x in itertools.permutations(string)]).intersection(words))

print(permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'}))
