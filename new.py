''' prime numbers '''
# l = [i for i in range(2,50) if i%2 != 0]

# for i in range(len(l)):
#     for j in range(2,i):
#         if (l[i]%j) == 0:
#             l[i] = False
#             break

# print([i for i in l if i is not False])

'''Fibonacci'''

# n = 10
# a = 0
# b = 1
# for i in range(n):
#     a,b = b,a+b
#     print(b, end = ' ')

'''Print simple pyramid of * pattern.'''

# n = 10
# for i in range(n):
#     for j in range(i):
#         print(j+1, end = ' ')
#     print('\n')


'''Factorial'''
# n = 7
# p = 1
# for i in range(1,n+1):
#     p = p*i

# print(p)

'''. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).'''

# for i in range (1500,2701):
#     if i%35 == 0:
#         print(i, end = ' ')

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*', end = ' ')
#     print('\n')
# for i in range(5,1,-1):
#     for j in range(1,i):
#         print('*', end = ' ')
#     print('\n')

# p = []
# for i in range(5):
#     q = [i*j for j in range(6)]
#     p.append(q)



# print(p)

# l = input()
# print(bool(l))

'''Determine which word has the greatest number of repeated letters.'''
# words = ['aerd', 'omqqqqqqqqqqqqqqqqqqqqqqar', 'fmmmmmruk', 'aaaxc', 'dasfsafsfadadfsafassdfsdfsdssfs']
# number_of_repeated_letters = []

# for word in words:
#     word_without_repeated_letter = list(set(word))
#     repeated_letter_number = len(word) - len(word_without_repeated_letter)
#     number_of_repeated_letters.append(repeated_letter_number)
# index = number_of_repeated_letters.index(max(number_of_repeated_letters))
# print(words[index])

'''Determine if three elements can sum to some larger number'''
# from itertools import combinations
# target = 50
# numbers = [21,45,84,3,2]
# comb = list(combinations(numbers,3))
# c =  False
# for i in comb:
#     if sum(i) == target :
#         c =  True
# print(c)

'''Determining the largest number of unique characters between two letters.'''
#c = 'deerf'
''' product of elements of a list without the item itself '''
nums = [6,2,3,4]
p = 1
n = len(nums)
output = []
for i in range(0,n):
    output.append(p)
    p = p * nums[i]
print(output)
p = 1
for i in range(n-1,-1,-1):
    output[i] = output[i] * p
    p = p * nums[i]
    print(p)

print(output)






