'''Determine if three elements can sum to some larger number'''
from itertools import combinations
target = 51
numbers = [21,45,84,3,2]
comb = list(combinations(numbers,3))
c =  False
for i in comb:
    if sum(i) == target :
        c =  True
print(c)