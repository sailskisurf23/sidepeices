userword = input("Enter word: ")
userwords = input("Enter list of words: ")

def anagrams(word, words):
    newword = ''.join(sorted(word))
    newwords = []
    for x in words:
        y = ''.join(sorted(x))
        newwords.append(y)
    truewords = []
    for z in range(len(newwords)):
        if newword == newwords[z]:
            truewords.append(words[z])
    return truewords

print(anagram(userword, userwords))
