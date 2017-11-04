x = input("input string")

def solution(s):
    slen = len(s)
    anslist = []
    if slen % 2 == 1:
        s = slen + "_"
    slen2 = len(s)
    ticker = 0
    while ticker < slen2:
        anslist.append(s[counter] + s[counter+1])
        ticker = ticker + 2
    return anslist

print(solution(x))
