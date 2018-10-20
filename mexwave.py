def make_upper(str, idx):
    str = str.lower()
    result = ''
    for i, char in enumerate(str):
        if i == idx:
            result += char.upper()
        else:
            result += char
    return result

def wave(str):
    r_list  = []
    for i, char in enumerate(str):
        if char == ' ':
            pass
        else:
            r_list.append(make_upper(str,i))
    return r_list


print(wave('hel lo'))


# print(make_upper('hello',4))
