def stringy(str1):
    output = ''
    for i in str1:
        output = output + i * int(i)
    return output

print(stringy('012'))


def compress(s):
    out = ''
    char, cnt = s[0], 0
    for i in s:
        if char == i:
            cnt += 1
        else:
            out += char + str(cnt)
            char = i
            cnt = 1
    return out

print(compress('aaabbddddccaaa'))


def func(l1,k):
    ind1,len1 = 0,0
    for i,x in enumerate(l1[:len(l1)-k+1]):
        str1 = ''.join(l[i:i+k])
        if len(str1) > len1:
            len1 = len(str1)
            ind1 = i
    return ''.join(l2[ind1:ind1+k])

func()
