def fib(num=1) :
    """Returns *num* integers of Fibonacci's sequence in list form"""
    fiblist = [0,1]
    counter = 0
    while counter + 2 < num:
        counter = counter + 1
        fiblist = fiblist + [fiblist[counter] + fiblist[counter-1]]
    if num == 1 :
        return [0]
    else:
        return fiblist

fibnum = int(input("How much of Fibonacci's sequence do you want to see? (enter integer)"))

print(fib(fibnum))             
             
