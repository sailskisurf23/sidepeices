#Ask user for Inputs
userinput1 = int(input("This program determines primality. Enter an integer greater than 0: "))

#Define function that returns divisors of a number
def divisor(number):
    divisors = []
    for x in range(1, (number+1)):
        if number % x == 0:
            divisors.append(x)
    return divisors

#apply divisor function to userinput1
divlist = divisor(userinput1)

#Print primality of userinput1
if len(divlist) <= 2 :
    print(str(userinput1) + " is a prime number")
else:
    print(str(userinput1) + " is NOT a prime number")
