#Purpose: Take a string or sentence and convert it into pig latin by removing
    #the first letter of each words and adding "ay" at the end of each word.

# Ask the user to enter a sentence
sentence = input('Enter your sentence in uppercase: ')

# Split the sentence into a list of words
words = sentence.split(' ')

# New list to contain Pig-Latin words
new_latin = []

# Convert new word to Pig Latin and add to new_words
for word in words:
    if word[-1].isalpha():
        new_latin.append(word[1 :]+ word[0] + 'AY')
    else:
        new_latin.append(word[1 : 1] + word[0] + 'AY' + word[-1])

# Join the list back together with spaces between words
new_sentence = ' '.join(new_latin)

# Display the new string in Pig Latin
print('\nHere\'s your sentence written in Pig Latin:')
print(new_sentence)
