def find_number(num, target):
    low = 0
    high = len(num)
    while low < high:
        mid = (low+high)//2
        if num[mid] == target:
            return mid
        if num[mid] < target:
            low = mid+1
        else: high = mid
    
    return False
num = [1,5,8,7,85]
target = 79
c =find_number(num, target)
print(c)