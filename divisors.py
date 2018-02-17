userinput = int(input("Enter integer: "))

divisors = []
for x in range(1, (userinput+1)):
    if userinput % x == 0:
        divisors.append(x)

for x in divisors:
    print(x)
