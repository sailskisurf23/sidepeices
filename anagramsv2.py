userword = input("Enter word: ")
userwords = input("Enter list of words: ")

def anagrams(word, words):
    newwords = []
    for item in words:
        if sorted(item) == sorted(word):
            newwords.append(item)
    return newwords

print(anagram(userword, userwords))
