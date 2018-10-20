
import time

t = 7
while t > 0:
    s=60
    while s > 0:
        print('You have {}:{} remaining'.format(t,s))
        time.sleep(1)
        s-=1
    t-=1
print("GAME OVER")
