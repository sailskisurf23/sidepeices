user = int(input('input max number for list'))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

x = []

for l in a :
    if l < user :
        x.append(l)

print(x)
