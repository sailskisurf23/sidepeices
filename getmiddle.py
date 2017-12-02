def get_middle(s):
    slen = len(s)
    char = slen / 2
    if slen % 2 == 0 :
        x = s[char-1] + s[char]
    else :
        x = s[char]
    return x
