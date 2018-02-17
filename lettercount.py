s = 'heLlo'.lower()
l = 'l'.lower()


result = 0
for x in s:
    if x == l:
        result += 1

# Print the number of times letter is in the inputted string
print(result)
