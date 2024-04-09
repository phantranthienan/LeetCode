# 198. House Robber

def rob(nums):
    if (len(nums) == 1):
            return nums[0]
    if (len(nums) == 2):
        return max(nums[0], nums[1])
    res = [nums[0], max(nums[0], nums[1])]
    for i in range(2, len(nums)):
        res.append(max(res[i - 2] + nums[i], res[i - 1]))
        
    return res[-1]