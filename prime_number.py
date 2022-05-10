def is_prime_number(num):
    for i in range(2,num):
        if num%i == 0:
            print(i)
            return False
    return True

print(is_prime_number(47))