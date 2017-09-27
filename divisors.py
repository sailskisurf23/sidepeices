userinput = int(input("Input integer and I will return Divisors"))

divisors = []

for x in range(1, userinput):
    if userinput % x == 0:
        divisors.append(x)

print(divisors)
