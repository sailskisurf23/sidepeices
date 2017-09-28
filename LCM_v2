#Ask user for Inputs
inputs = []
while True:
    inp = input("This program returns the LCM, Enter an integer,\
    enter nothing after last integer to be evaluated: ")
    if inp == "":
        break
    inputs.append(int(inp))

#Define function that returns LCM
def lcm(*args):
    """ Returns the least common multiple of 'args' """
    #Initialize counter & condition
    counter = 1
    condition = False

    #While loop iterates until LCM condition is satisfied
    while condition == False :
        counter = counter + 1
        xcondition = []
        for x in args:
            xcondition.append(counter % x == 0)
        if False in xcondition:
            condition = False
        else:
            condition = True
    return counter

#Execute function on inputs
result = lcm(inputs)

#Print Result
print(result)
