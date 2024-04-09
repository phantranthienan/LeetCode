# 300. Longest Increasing Subsequence
def lengthOfLIS(nums):
    n = len(nums)
    listDp = [1] * len(nums)

    for i in range(n):
        for j in range(1, i):
            if nums[j] > nums[i]:
                nums[j] = max(nums[j], nums[i] + 1)
    
    return max(listDp)
            


