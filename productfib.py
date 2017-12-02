def fib(num=1) :
    """Returns the num index of Fibonacci's sequence"""
    fiblist = [0,1]
    counter = 0
    while counter <= num + 1:
        counter = counter + 1
        fiblist = fiblist + [fiblist[counter] + fiblist[counter-1]]
    return fiblist[num]

def productFib(prod):
    counter = 0
    fibprod = 0
    while fibprod <= prod:
        counter += 1
        fibprod = fib(counter-1) * fib(counter)
        
    return [fib(counter), fib(counter + 1), fibprod == prod], fibprod

userinput = int(input("INPUT PROD: "))
print(productFib(userinput))
