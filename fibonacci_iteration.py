def fibonacci(num):
    if num == 1:
        return 1
    a = 0
    b = 1

    for i in range(1,num):
        a,b = b, a+b
    return a

print(fibonacci(0))
