'''Write a program to reverse an integer in Python'''
def reverse_number(num):
    rev_num = 0
    while num > 1:
        rev_num = rev_num*10 + num % 10
        num = num // 10
    return rev_num

print(reverse_number(56252145))