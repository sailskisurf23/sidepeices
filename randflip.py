import random

def flip_coin(p=0.5):
    '''
    Using random.random() simulate flipping a coin where the probability of
    flipping a head is p.

    Parameters
    ----------
    p: {float} probability of flipping a head (must be between 0 and 1)

    Returns
    -------
    flip: {str} "H" if coin is heads, otherwise "T"
    '''
    if random.random() < p:
        return 'H'
    else:
        return 'T'

print(flip_coin())
