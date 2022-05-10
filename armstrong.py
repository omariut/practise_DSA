'''Write a program in Python to check whether an integer is Armstrong number or not.'''
def get_armstrong_number (num):
    s = 0
    count = 0
    number = num 
    
    while num >= 1:
        num = num//10
        count += 1
    num = number 
    while num >= 1:
        s += (num % 10) ** count
        num = num//10
    return s == number
print(get_armstrong_number(1634))