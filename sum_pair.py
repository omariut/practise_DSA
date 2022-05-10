
# #first approach
# def find_number(num, target):
#     low = 0
#     high = len(num) -1
#     num.sort()
#     while low < high:
#         if num[low] + num[high] == target:
#             return num[low], num[high]
        
#         if  num[low] + num[high] > target:
#             high = high - 1
#         else:
#             low = low + 1
    
#     return False
import time
def find_number(num, target):

    d= {}
    for i,e in enumerate(num):
        if target - e in d:
            return  d[target-e], i
        d[e] = i
    return False

num = [1,5,8,7,85]
target = 86
start = time.time()
c =find_number(num, target)
end = time.time()
print((end - start)*10**6)
print(c)