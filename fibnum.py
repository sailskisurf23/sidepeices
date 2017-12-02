def fib(num=1) :
    """Returns the num index of Fibonacci's sequence"""
    fiblist = [0,1]
    counter = 0
    while counter <= num + 1:
        counter = counter + 1
        fiblist = fiblist + [fiblist[counter] + fiblist[counter-1]]
    return fiblist[num]

fibnum = int(input("Enter index of Fibonacci Sequence (enter integer)"))

print(fib(fibnum))
