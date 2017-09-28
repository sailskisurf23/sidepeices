#Ask user for Inputs
userinput1 = int(input("This program returns the GCD of two integers, Enter first integer: "))
userinput2 = int(input("Enter second integer: "))

#Define gcd function
def gcd(x,y):
    """Returns the Greatest Common Denominator of two integers x & y"""
    #Initialize counter & condition
    counter = max(x,y)
    condition = False
    #Count down from larger of two numbers until GCD condition is satisfied
    while condition == False :
        counter = counter - 1
        condition = (x % counter == 0) and (y % counter == 0)
    return counter

#Print Result
result = gcd(userinput1,userinput2)
print( "The Greatest Common Denominator of " + str(userinput1)
+ " and " + str(userinput2) + " is " + str(result))
