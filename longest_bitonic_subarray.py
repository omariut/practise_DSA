def longest_bitonic_subarray(nums):
    asc = False
    desc = False
    asc_count = 0
    desc_count = 0
    pivot = 0
    count = 0
    for i in range(1,len(nums)):
        if nums[i-1] < nums[i]:
            asc = True
        
        if nums[i-1] > nums[i]:
            desc = True
        
        if asc == True and desc == False:
            asc_count+=1
        
        if asc == False and desc == True:
            desc_count+=1
        
        if asc == True and desc == True:
            count += asc_count + desc_count
            asc = False
            desc = False
            asc_count = 0
            desc_count = 0

            
        
    return 

a = [ 3, 5, 8, 4, 3, 9, 10, 8, 5, 3, 4]
x = longest_bitonic_subarray(a)
print(x)

        


