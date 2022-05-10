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