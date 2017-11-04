#Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

#Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

#If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

#For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

userinput = input("Input your sentence: ")

def order(sentence):
    #Split setnence into list
    senlist = sentence.split()
    #Create new list in correct order
    newlist = []
    for i in range(1,10):
        for word in senlist:
            if str(i) in word:
                newlist.append(word)

    #Turn list back into string
    return " ".join(newlist)

print(order(userinput))
