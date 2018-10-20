
def accum(s):
    result = ""
    for i,char in enumerate(s):
        result += (char*(i+1)).capitalize() + '-'
    return result.strip('-')

def accum2(s):
    return '-'.join([(char*(i+1)).capitalize() for i,char in enumerate(s)]).strip('-')

print(accum2("abcd"))
