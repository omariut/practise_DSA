def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    print(num)
    return fibonacci(num-1)+fibonacci(num-2)

fibonacci(4)