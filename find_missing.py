seq1 = [1,2,3,4,6,7,8,9]
seq2 = [2,6,8,10]
seq3 = [3,5,7,11,13]

def find_missing(sequence):
    difflist = [(sequence[x+1] - sequence[x]) for x in range(len(sequence)-1)]

    for diff in difflist:
        if difflist.count(diff) == 1: baddiff = diff
        if difflist.count(diff) >= 1: gooddiff = diff

    return sequence[difflist.index(baddiff)] + gooddiff

print(find_missing(seq2))
