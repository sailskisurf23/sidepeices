def most_common(s):
    '''
    Write a function that takes in a paragraph and returns the most
    common word. Not case sensitive.

    HINT: A dictionary might be useful!

    eg. IN: "The red dog jumped over the black dog. I liked the red dog."
        OUT: "dog"
    '''
    # First split the string into a list of words
    # strip out all punctuation
    # make everything lowercase
    wordlist = [x.strip('. ').lower() for x in s.split()]
    # Now we initialize a dictionary (keys are words, values are counts)
    resultdict = {}
    # Loop through list of words.
    for word in wordlist:
        # If word is already in dictionary, increment count by 1
        if word in resultdict.keys():
            resultdict[word] += 1
        # If word is new, add it to dict and set count value to 1
        else:
            resultdict[word] = 1
    # initialize winning key ('word') and winning value ('count')
    winnerk = ''
    winnerv = 0
    # Loop through each key,value pair in dictionary
    for k, v in resultdict.items():
        # If count is greater than current winner, update winning key and value
        if v > winnerv:
            winnerk = k
            winnerv = v
    # Return winning key
    return winnerk
