def sen_capperA(s):
    '''
    Write a function that takes in a string s and returns a string with the
    first letter of each sentence Capitalized and the rest of the letters are
    lowercase

    HINT: Helpful methods .split(), .join(), .upper(), .lower(), .strip()

    eg. IN: "Mary HAD a LITTLE Lamb.   HER NAME WAS KArey."
        OUT: Mary had a little lamb. Her name was karey.

    '''
    # First we split our string into a list of sentences
    sen_list = s.split('. ')
    print(sen_list)
    # Now let's strip of the whitespace from each sentence
    sen_list2 = [x.strip() for x in sen_list]
    print(sen_list2)
    # Now Cap the first letter of each sentence and make the rest lowercase
    sen_list3 = [x[0].upper() + x[1:].lower() for x in sen_list2]
    print(sen_list3)
    # Now we join our list of sentences back togeether
    # into a single string separated by a period
    new_s = '. '.join(sen_list3)
    return new_s

def sen_capperB(s):
    '''
    This code works the same as the function above,
    but is written more Pythonically ;)
    '''
    return '. '.join(x.strip()[0].upper() + x.strip()[1:].lower() for x in s.split('. '))


# Here is my test block
s = 'MARY had A LITtle Lamb.   her FLEEcE waS White aS SNow.'

print(sen_capperA(s))
