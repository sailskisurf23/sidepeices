from sys import argv
import io
import pandas as pd


#import, open and read text file; txt file should use UTF-8
script, filepath = argv
otxt = io.open(filepath,'r',encoding='utf8')
txt = otxt.read()

def word_count(txt=txt):
    #split file into list of words, then find length of list
    return len(txt.split())

def sentence_count(txt=txt):
    #split file into list of sentences, then find length of list
    return len(txt.split('.'))

def unique_words(txt=txt):
    #split file into list of unique_words, strip common punctuation, lowercase to avoid dupes from capitals
    wordlist = txt.strip('.,!?').lower().split()
    #loop through wordlist, and add new words to a new list.
    newwordlist = []
    for x in wordlist:
        if x not in newwordlist:
            newwordlist.append(x)
    return len(newwordlist)

def average_sentence_length(txt=txt):
    #create list of sentences
    sentences = txt.split('.')
    #create list of sentence_lengths:
    #split each sentence and finding the length of resulting string
    sentence_lengths = []
    for x in sentences:
        sentence_lengths.append(len(x.split()))
    #compute average from sentence_lengths list
    #use max function to avoid error if len(sentence_lengths) == 0
    return sum(sentence_lengths)/max(len(sentence_lengths),1)

def oft_used_phrase(txt=txt):
    #split file into words
    wordlist = txt.lower().split()
    #split file into 3 word phrases, increment by one so that each 3 word phrase possibility is captured
    phrases = []
    for x in range(0,len(wordlist)):
        phrases += [wordlist[x:x+3]]
    #identify unique phrases
    unique_phrases = []
    for x in phrases:
        if x not in unique_phrases:
            unique_phrases.append(x)
    #count occurences of each unique phrase
    unique_phrases_counts = []
    for x in unique_phrases:
        unique_phrases_counts.append(phrases.count(x))
    #zip unique phrases together with their counts and return DataFrame containing only those which have 3 or more occurences
    #would be nice to dedup so that phrases that are more than 3 words long aren't double counted as separate phrase
    phrase_counts = pd.DataFrame(list(zip(unique_phrases, unique_phrases_counts)),columns=['phrases','counts'])
    return phrase_counts[phrase_counts.counts >= 3]

def unique_words_sorted(txt=txt):
    #split file into list of unique_words, strip common punctuation, lowercase to avoid dupes from capitals
    wordlist = txt.strip('.,!?').lower().split()
    #loop through wordlist, and add new words to a new list.
    unique_words = []
    for x in wordlist:
        if x not in unique_words:
            unique_words.append(x)
    #loop through unique words and count occurences
    unique_word_counts = []
    for x in unique_words:
        unique_word_counts.append(wordlist.count(x))
    #zip together, put in DF, sort, return list of unique words
    word_counts = pd.DataFrame(list(zip(unique_words,unique_word_counts)),columns=['words','counts'])
    return list(word_counts.sort_values('counts',ascending=False)['words'])

varword_count = word_count()
varunique_words = unique_words()
varsentence_count = sentence_count()
varaverage_sentence_length = average_sentence_length()
varoft_used_phrase = oft_used_phrase()
varunique_words_sorted = unique_words_sorted()

print(
f' \n',
f'TEXT ANALYSIS: \n',
f'Filepath: {filepath} \n',
f'Word Count: {varword_count} words \n',
f'Unique Word Count: {varunique_words} unique words \n',
f'Sentence Count: {varsentence_count} sentences \n',
f'Average Sentence Length: {varaverage_sentence_length} words \n',
f'Phrases used more than 3 times: \n'
f'{varoft_used_phrase} \n \n'
f'10 Most Common Words: {varunique_words_sorted[:11]} \n'
)

#close file
otxt.close()
