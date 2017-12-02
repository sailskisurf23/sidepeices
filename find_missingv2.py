seq1 = [1,2,3,4,6,7,8,9]
seq2 = [2,6,8,10]
seq3 = [3,5,7,11,13]

def find_missing(sequence):
    difflist = [(sequence[x+1] - sequence[x]) for x in range(2)]
    gooddiff = min(difflist)
    dd = 0
    answer = sequence[0]
    while sequence[dd+1] - sequence[dd] == gooddiff:
        dd += 1
        answer += gooddiff

    return answer + gooddiff

print(find_missing(seq3))
