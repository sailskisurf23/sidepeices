str1 = "abcd\nefgh\nijkl\nmnop"

def rot(s):
    return s[::-1]

def selfie_and_rot(s):
    s_list1 = [x + '.'*len(s.splitlines()) for x in s.splitlines()]
    s_list2 = ['.'*len(s.splitlines()) + x for x in rot(s).splitlines()]
    return ''.join([x+'\n' for x in s_list1 + s_list2])

def oper(fct, s):
    if fct == rot:
        return rot(s)
    elif fct == selfie_and_rot:
        return selfie_and_rot(s)



print(oper(selfie_and_rot,str1))
