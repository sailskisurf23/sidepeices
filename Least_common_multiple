#Ask user for Inputs
userinput1 = int(input("This program returns the LCM of two integers, Enter first integer: "))
userinput2 = int(input("Enter second integer: "))

#Define function that returns LCM
def lcm(x,y):
    """Returns the least common multiple of two integers x & y"""
    #Initialize counter & condition
    counter = 1
    condition = False
    #While loop iterates until LCM condition is satisfied
    while condition == False :
        counter = counter + 1
        condition = (counter % x == 0) and (counter % y == 0)
    return counter

#Execute function
result = lcm(userinput1,userinput2)

#Print Result
print( "The Least Common Multiple of " + str(userinput1)
+ " and " + str(userinput2) + " is " + str(result))
