import time

m = int(input('Please enter the number of minutes remaining: '))
m -= 1
while m >= 0:
    s=59
    while s >= 0:
        print('You have {}:{} remaining'.format(m,s))
        time.sleep(1)
        s -= 1
    m -= 1

print("Time's up!!")
