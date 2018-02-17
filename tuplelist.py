nums = '1, 2, 3, 4, 5, 6, 7'
numlist = nums.split(',')
intlist = [int(x) for x in numlist]
l1 = []
l2 = []
for i in range(len(intlist)):
    if i % 2 == 0:
        l1.append(intlist[i])
    if i % 2 != 0:
        l2.append(intlist[i])

tlist = list(zip(l1,l2))
print(tlist)
