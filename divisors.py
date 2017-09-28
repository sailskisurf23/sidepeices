userinput = int(input("This program returns the divisors of input value. Enter integer: "))

divisors = []
for x in range(1, (userinput+1)):
    if userinput % x == 0:
        divisors.append(x)

print(divisors)
