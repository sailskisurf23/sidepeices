def narcissistic( value ):
    strval = str(value)
    vlen = len(strval)
    listval = []
    intsum = 0
    for x in strval:
        listval.append(int(x))
    for y in listval:
        intsum += y**vlen
    return intsum == value
