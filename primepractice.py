def is_prime(n):
    '''
    Return True if the input is prime, False otherwise
    Parameters
    ----------
    n: {int} input integer

    Returns
    -------
    is_prime: {bool} whether n is prime
    '''
    result = True
    for x in range(2,n-1):
        if n % x == 0:
            result = False
    if n == 0:
        result = False
    return result

print(is_prime(0))
