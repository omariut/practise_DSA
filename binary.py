'''Check if a number is binary'''

def find_binary(num):
    b = [0,1]
    while num >= 1:
        q = num%10
        if q not in b :
            return False
        num //= 10
    return True

print(find_binary(10110001))