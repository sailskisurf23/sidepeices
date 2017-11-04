uservar = int(input("Enter an integer you would like to factorialize: "))

def factorialize(var1):
    """Returns the factorial of var1 using for loop"""
    result = 1
    for x in range(1,var1+1) :
        result = result * x
    return result

print(str(uservar) +"! = " + str(factorialize(uservar)))
