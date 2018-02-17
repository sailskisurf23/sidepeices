nums = '1, 2, 3, 4, 5, 6, 7'
numlist = nums.split(',')
intlist = [int(x) for x in numlist]
sqrlist = [x**2 for x in intlist]
sqrdict = {k:v for k,v in zip(intlist,sqrlist)}
print(sqrdict)
