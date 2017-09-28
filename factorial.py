uservar = int(input("Enter an integer you would like to factorialize: "))

def factorialize(var1):
    """Returns the factorial of var1"""
    counter = 1
    result = 1
    while counter <= var1:
        result = result * counter
        counter = counter + 1
    return result

print(str(uservar) +"! = " + str(factorialize(uservar)))
