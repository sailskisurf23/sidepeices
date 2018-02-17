def find_number(start=1, stop=10, string='1234567891011'):
    a = list(range(start,stop+1))
    b = ''
    for x in a:
        b += str(x)
    c = list(string)
    d = list(b)
    for x in list(b):
        c.remove(x)
    return ''.join(c)

print(find_number())
