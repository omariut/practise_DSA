def lengthOfLongestSubstring(s):
    if len(s) == 0:
        
        return 0
    left, right = 0, 0
    longest = 1
    seen = {}
    for i in range(len(s)):
        if s[right] in seen:
            left = max(left,seen[s[right]] + 1)
        if longest <= right - left +1 :
            right_index = right
            left_index = left 
        longest = max(longest, right - left + 1)
        
        seen[s[right]] = right
        right+=1
    return left_index, right_index

nums =[2, 0, 0, 1, 4, 3, 7, 0]
c =lengthOfLongestSubstring(nums)
print(c)