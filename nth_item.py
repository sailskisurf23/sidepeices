number = int(input('Please enter a value for N: '))

series = [1]
for x in range(number):
    item = 2*series[-1] + 1
    series.append(item)

print(series[-1])
