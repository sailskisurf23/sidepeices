str1="*'&ABCDabcde12345"
result= [4,5,5,3]
#the order is: uppercase letters, lowercase, numbers and special characters.

def solve(s):
    uc = list(map(chr, range(65, 91)))
    lc = list(map(chr, range(97, 123)))
    nm = list(map(chr, range(48, 58)))

    result = [0,0,0,0]
    for char in s:
        if char in uc:
            result[0] += 1
        elif char in lc:
            result[1] += 1
        elif char in nm:
            result[2] += 1
        else:
            result[3] += 1
    return result

def dbl_linear(n):
    dbl_set = {1}
    while len(dbl_set) < n**2:
        dbl_set1 = {2*x+1 for x in dbl_set}
        dbl_set2 = {3*x+1 for x in dbl_set}
        dbl_set = dbl_set | dbl_set1 | dbl_set2
    return sorted(list(dbl_set))[n]


from collections import deque

def dbl_linear2(n):
    h = 1; cnt = 0; q2, q3 = deque([]), deque([])
    while True:
        if (cnt >= n):
            return h, q2, q3
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0], q3[0])
        if h == q2[0]: h = q2.popleft()
        if h == q3[0]: h = q3.popleft()
        cnt += 1


def count_repeats(s):
    result = 0
    for i,x in list(enumerate(s))[1:]:
        if x == s[i-1]:
            result += 1
    return result

print(count_repeats('ab cca'))


deque
cycle
