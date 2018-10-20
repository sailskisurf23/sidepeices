'''
Write a script that prints the first N digits of the fibbonacci sequence

0,1,1,2,3,5,8,13...

Bonus points if you can store it into a list.

'''

n = 4
#counter = 2
fib_list = [0,1]

while len(fib_list) < n:
    next_num = fib_list[-1] + fib_list[-2]
    fib_list.append(next_num)
    # counter += 1

print(fib_list)
