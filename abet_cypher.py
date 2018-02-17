import string
import math

def encode(message, key):
    letterdict = {y:x for (x,y) in enumerate('0'+string.ascii_lowercase)}
    numlist = [letterdict[z] for z in message]
    keylist = [int(a) for a in math.ceil(len(message)/ len(str(key))) * str(key)]
    return [b+c for b,c in list(zip(numlist,keylist))]

if __name__ == '__main__':
    message = 'scout'
    key = 1939
    print(encode(message,key))
