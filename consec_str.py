import numpy as np

def longest_consec(arr,num):
    len_arr = [len(x)for x in arr]
    sum_arr = [sum(len_arr[i:i+num]) for i,x in enumerate(len_arr) ]
    max_idx = np.argmax(sum_arr)
    return ''.join(arr[max_idx:max_idx+num])






print(consec(["zone", "abigail", "theta",
"form", "libe", "zas", "theta", "abigail"], 2))
