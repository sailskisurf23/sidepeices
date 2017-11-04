import random

a = []
b = []
common = []

for x1 in range(1,random.randint(5,20)):
    a.append(random.randint(1,10))

for x2 in range(1,random.randint(5,20)):
    b.append(random.randint(1,10))

for x in a:
    if x in b and x not in common:
        common.append(x)

common.sort()

print("list a : " + str(a))
print("list b : " + str(b))
print("list elements in common : " +str(common))

