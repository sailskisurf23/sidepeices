def find_even_index(arr):
    answer = -1
    arraylen = len(arr)
    for x in range(arraylen):
        if sum(arr[:x]) == sum(arr[x+1:]):
            answer = x
            break
    return answer
