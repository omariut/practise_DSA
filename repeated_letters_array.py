'''Determine which word has the greatest number of repeated letters.'''
words = ['aerd', 'omqqqqqqqqqqqqqqqqqqqqqqar', 'fmmmmmruk', 'aaaxc', 'dasfsafsfadadfsafassdfsdfsdssfs']
number_of_repeated_letters = []

for word in words:
    word_without_repeated_letter = list(set(word))
    repeated_letter_number = len(word) - len(word_without_repeated_letter)
    number_of_repeated_letters.append(repeated_letter_number)
index = number_of_repeated_letters.index(max(number_of_repeated_letters))
print(words[index])