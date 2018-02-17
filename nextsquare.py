def next_perfect_square(n):
    '''
    Returns the next perfect square of the input number, if the input number
    is not a perfect square, returns -1.
    Ex:
    next_perfect_square(10)
    >>> -1
    next_perfect_square(9)
    >>> 16
    next_perfect_square(25)
    >>> 36
    next_perfect_square(37)
    >>> -1

    Parameters
    ----------
    number: {int}

    Returns
    -------
    next_perfect: {int} the next perfect square, or -1 if number is not a
    perfect square
    '''
    if is_perfect_square(n) == False:
        return -1
    else:
        for x in range(n):
            if x**2 == n:
                return (x+1)**2
