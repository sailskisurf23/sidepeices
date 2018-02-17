def count_pair_sums(arr, number=0):
    '''
    Given an array, find the count of how many pairs of numbers in the array sum
    to the input number

    Parameters
    ----------
    arr: {list} list of integers (positive and negative)
    number: number to see if pairs sum to (default 0)

    Returns
    -------
    pairs: {list of {tuple}} the pairs found that sum to given number
    '''
    tuplist = []
    for i in range(len(arr)):
        for i2 in range(i+1,len(arr)):
            tuplist.append((arr[i],arr[i2]))
    tuplist2 = []
    for x in tuplist:
        if x[0] + x[1] == number:
            tuplist2.append(x)
    return len(tuplist2)

print(count_pair_sums([1,2,3,4],0))

1 1 1
1 1 1 and

1 1 1 1
1 1 1 1
1 1 1 1
